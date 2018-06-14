import datetime

from django.contrib.auth.models import User
from django.db import models
from django_facebook.models import FacebookModel

from revolv.base.utils import get_group_by_name, get_profile
from revolv.lib.utils import ImportProxy
from revolv.payments.models import Payment


class RevolvUserProfileManager(models.Manager):
    def create_user(self, *args, **kwargs):
        """
        For purposes of testing and DRYness, it is often useful to create
        a user and return the associated RevolvUserProfile.
        """
        user = User.objects.create_user(*args, **kwargs)
        return get_profile(user)

    def create_user_as_ambassador(self, *args, **kwargs):
        """Create a user, assign it to be an ambassador, and return its profile."""
        profile = self.create_user(*args, **kwargs)
        profile.make_ambassador()
        return profile

    def create_user_as_admin(self, *args, **kwargs):
        """Create a user, assign it to be an admin, and return its profile."""
        profile = self.create_user(*args, **kwargs)
        profile.make_administrator()
        return profile

    def get_subscribed_to_newsletter(self, queryset=None):
        """ Gets all the RevolvUserProfile objects that are
        currently subscribed to the newsletter. It also orders the queryset
        by order which the user joined.

        :queryset: The queryset in which to search for users
        :return: A queryset of RevolvUserProfile objects sorted by date joined
        """
        if queryset is None:
            queryset = super(RevolvUserProfileManager, self).get_queryset()
        subscribed_users = queryset.filter(
            subscribed_to_newsletter=True
        ).order_by('user__date_joined')
        return subscribed_users


class RevolvUserProfile(FacebookModel):
    """
    A simple wrapper around django-facebook's FacebookModel, which contains
    Facebook information like name, etc. RevolvUserProfile ties a FacebookModel
    and a django auth.User model together, so that we can use both Facebook
    and non-Facebook user profiles.

    Note: there are three main roles that users in the Revolv application can
    occupy: donor, ambassador, and admin.

    Donors are regular users, who can donate to projects and see the impact of
    their donations.

    Ambassadors are users who can donate AND create projects, to be
    approved by the admin. Note: ambassadors are NOT staff with respect to the
    django User model, since we use the is_staff boolean to check whether the
    django CMS toolbar is visible for users.

    Admins are users who can approve and manage projects, AND control whether
    other users are ambassadors or admins themselves. Admins can also donate to
    projects like regular donors can. Every admin's User model has is_staff = True
    in order to see the django-cms toolbar on the homepage.
    """
    objects = RevolvUserProfileManager()
    factories = ImportProxy("revolv.base.factories", "RevolvUserProfileFactories")

    AMBASSADOR_GROUP = "ambassadors"
    ADMIN_GROUP = "administrators"

    user = models.OneToOneField(User)
    subscribed_to_newsletter = models.BooleanField(default=False)
    zipcode = models.CharField(max_length=10, null=True, blank=True, default="")
    subscribed_to_updates = models.BooleanField(default=False)
    subscribed_to_repayment_notifications = models.BooleanField(default=True)

    reinvest_pool = models.FloatField(default=0.0)
    solar_seed_fund_pool = models.FloatField(default=0.0)
    preferred_categories = models.ManyToManyField("project.Category")

    address = models.CharField(max_length=255, null=True, blank=True)

    def is_donor(self):
        """Return whether the associated user can donate."""
        return True

    def is_ambassador(self):
        return get_group_by_name(
            self.AMBASSADOR_GROUP
        ) in self.user.groups.all()

    def is_administrator(self):
        return get_group_by_name(self.ADMIN_GROUP) in self.user.groups.all()

    def make_administrator(self):
        self.user.groups.add(get_group_by_name(self.AMBASSADOR_GROUP))
        self.user.groups.add(get_group_by_name(self.ADMIN_GROUP))
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()

    def make_ambassador(self):
        self.user.is_staff = False
        self.user.is_superuser = False
        self.user.groups.remove(get_group_by_name(self.ADMIN_GROUP))
        self.user.groups.add(get_group_by_name(self.AMBASSADOR_GROUP))
        self.user.save()

    def make_donor(self):
        """Take away all the user's permissions."""
        self.user.is_staff = False
        self.user.is_superuser = False
        self.user.groups.remove(get_group_by_name(self.ADMIN_GROUP))
        self.user.groups.remove(get_group_by_name(self.AMBASSADOR_GROUP))
        self.user.save()

    def user_impact_for_watts(self):
        all_payments = Payment.objects.payments(user=self).exclude(project__isnull=True)
        user_impact = 0
        for payment in all_payments:
            project = payment.project
            if project:
                user_financial_contribution = payment.amount
                project_funding_total = (int)(project.funding_goal)
                expected_KW_Output = project.impact_power
                per_dollor_generated_energy = (expected_KW_Output / project_funding_total)
                user_impact_for_watt = float(per_dollor_generated_energy) * float(user_financial_contribution)*1000
                user_impact += user_impact_for_watt
        return user_impact

    def user_impact_for_carbon_dioxide(self):
        all_payments = Payment.objects.payments(user=self).exclude(project__isnull=True)
        user_impact = 0
        POUNDS_CARBON_PER_KWH = 1.5
        for payment in all_payments:
            project = payment.project
            if project:
                user_financial_contribution = payment.amount
                project_funding_total = (int)(project.funding_goal)
                total_kwh_value = project.total_kwh_value
                carbon_dioxide_avoided_by_project = float(POUNDS_CARBON_PER_KWH) * float(total_kwh_value)
                per_dollor_avoided_co2 = carbon_dioxide_avoided_by_project/project_funding_total
                user_impact_for_carbon_dioxide = per_dollor_avoided_co2 * user_financial_contribution
                user_impact += user_impact_for_carbon_dioxide
        return user_impact

    def user_impact_of_acr_of_tree_save(self):
        all_payments = Payment.objects.payments(user=self).exclude(project__isnull=True)
        user_impact = 0
        ACRE_OF_TREES_PER_KWH = 0.0006
        for payment in all_payments:
            project = payment.project
            if project:
                user_financial_contribution = payment.amount
                project_funding_total = (int)(project.funding_goal)
                total_kwh_value = project.total_kwh_value
                acre_of_tree_save_by_project = float(ACRE_OF_TREES_PER_KWH) * float(total_kwh_value)
                per_dollor_saved_trees = acre_of_tree_save_by_project / project_funding_total
                # print ("aaaa", acr_of_tree_save_by_project,per_dollor_saved_trees)
                user_impact_for_saved_trees = per_dollor_saved_trees * user_financial_contribution
                user_impact += user_impact_for_saved_trees
        return user_impact

    def get_statistic_for_user(self, attr):
        """Calculates a user's individual impact by iterating through all the users payments, calculating
        what fraction of that project comprises of this user's donation, and calculates individual
        user impact using the statistics attribute (a KilowattStatsAggregator) and the fraction."""
        all_payments = Payment.objects.payments(user=self).exclude(project__isnull=True)
        user_impact = 0
        for payment in all_payments:
            project = payment.project
            if project:
                user_financial_contribution = payment.amount
                project_funding_total = (int)(project.funding_goal)
                project_impact = getattr(project.statistics, attr)
                user_impact_for_project = project_impact * user_financial_contribution * 1.0 / project_funding_total
                user_impact += user_impact_for_project
        return user_impact

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.user.first_name.strip(), self.user.last_name.strip())
        if len(full_name.strip()) == 0:
            full_name = self.user.username
        return full_name.strip()

    def get_username(self):
        """
        Returns the first_name plus the first initial of last_name, with a space in between.
        """
        full_name = '%s %s' % (self.user.first_name.strip(), self.user.last_name.strip()[0:1])
        if len(full_name.strip()) == 0:
            full_name = self.user.username
        return full_name.strip()
