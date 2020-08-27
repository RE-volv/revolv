import datetime
from itertools import chain

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q, Sum
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from revolv.base.models import RevolvUserProfile
from revolv.lib.utils import ImportProxy
from revolv.payments.models import Payment, PaymentType
from revolv.project.stats import KilowattStatsAggregator


class ProjectManager(models.Manager):
    """
    Manager for running custom operations on the Projects.
    """

    def get_featured(self, num_projects, queryset=None):
        """ Get num_projects amount of active projects. If we don't have
        enough active projects, then we retrieve completed projects. This
        function may return fewer projects than requested if not enough exist.

        :num_projects: Number of projects to be retrieved
        :queryset: The queryset in which to search for projects
        :return: A list of featured project objects
        """
        if queryset is None:
            queryset = super(ProjectManager, self).get_queryset()
        featured_projects = queryset.filter(
            project_status=Project.ACTIVE).order_by(
            'end_date')[:num_projects]
        if featured_projects.count() < num_projects:
            num_completed_needed = num_projects - featured_projects.count()
            completed_projects = queryset.filter(
                project_status=Project.COMPLETED).order_by(
                'end_date')[:num_completed_needed]
            return list(chain(featured_projects, completed_projects))
        else:
            return featured_projects

    def get_total_avoided_co2(self, queryset=None):
        """ Gets all the projects that have been completed funding.

        :queryset: The queryset in which to search for projects
        :return: A list of completed project objects
        """
        user_impact = 0
        POUNDS_CARBON_PER_KWH = 1.5
        if queryset is None:
            projects = super(ProjectManager, self).get_queryset()
        for project in projects:
            project_funding_total = (int)(project.funding_goal)
            amount_donated = (int)(project.amount_donated)
            project_total_kwh_value = project.total_kwh_value
            per_project_avoided_co2 = float(project_total_kwh_value) * POUNDS_CARBON_PER_KWH
            project_impact = float(per_project_avoided_co2 * amount_donated) / float(project_funding_total)
            user_impact += project_impact
        return user_impact

    def get_completed(self, queryset=None):
        """ Gets all the projects that have been completed funding.

        :queryset: The queryset in which to search for projects
        :return: A list of completed project objects
        """
        if queryset is None:
            queryset = super(ProjectManager, self).get_queryset()
        completed_projects = queryset.filter(
            project_status=Project.COMPLETED
        ).order_by('end_date').reverse().exclude(org_name='SSF').exclude(org_name='SUBSF')
        return completed_projects

    def get_completed_ssf(self, queryset=None):
        """ Gets all the projects that have been completed funding for solar seed fund.

        :queryset: The queryset in which to search for projects
        :return: A list of completed project objects
        """
        if queryset is None:
            queryset = super(ProjectManager, self).get_queryset()
        completed_projects = queryset.filter(
            project_status=Project.COMPLETED,  org_name='SSF').order_by('end_date')

        return completed_projects

    def get_active(self, queryset=None):
        """ Gets all the projects that have been active to go into funding.

        :queryset: The queryset in which to search for projects
        :return: A list of active project objects
        """
        if queryset is None:
            queryset = super(ProjectManager, self).get_queryset()
        active_projects = queryset.filter(
            project_status=Project.ACTIVE
        ).order_by('end_date').exclude(org_name='SSF').exclude(org_name='SUBSF').exclude(org_name='MAINSSF')
        return active_projects

    def get_active_fundraiser(self, queryset=None):
        """ Gets all the projects that have been active to go into funding.

        :queryset: The queryset in which to search for projects
        :return: A list of active project objects
        """
        if queryset is None:
            queryset = super(ProjectManager, self).get_queryset()
        active_projects = queryset.filter(
            project_status__in=[Project.ACTIVE, Project.COMPLETED], org_name='SSF'
        ).order_by('end_date')
        return active_projects


    def get_active_and_main_fundraiser(self, queryset=None):
        """ Gets all the projects that have been active to go into funding.

        :queryset: The queryset in which to search for projects
        :return: A list of active project objects
        """
        if queryset is None:
            queryset = super(ProjectManager, self).get_queryset()
        active_projects = queryset.filter(
            project_status=Project.ACTIVE, org_name__in=['SSF', 'MAINSSF']
        ).order_by('end_date')
        return active_projects

    def get_main_active_fundraiser(self, queryset=None):
        """ Gets all the projects that have been active to go into funding.

        :queryset: The queryset in which to search for projects
        :return: A list of active project objects
        """
        if queryset is None:
            queryset = super(ProjectManager, self).get_queryset()
        active_projects = queryset.filter(
            project_status=Project.ACTIVE, org_name='MAINSSF'
        ).order_by('end_date')
        return active_projects


    def get_active_subfundraiser(self, queryset=None):
        """ Gets all the projects that have been active to go into funding.

        :queryset: The queryset in which to search for projects
        :return: A list of active project objects
        """
        if queryset is None:
            queryset = super(ProjectManager, self).get_queryset()
        active_projects = queryset.filter(
            project_status=Project.ACTIVE, org_name='SUBSF'
        ).order_by('end_date')
        return active_projects

    def get_proposed(self, queryset=None):
        """ Gets all the projects that are currently in review (proposed).

        :queryset: The queryset in which to search for projects
        :return: A list of in review project objects
        """
        if queryset is None:
            queryset = super(ProjectManager, self).get_queryset()
        proposed_projects = queryset.filter(
            project_status=Project.PROPOSED
        ).order_by('updated_at')
        return proposed_projects

    def get_drafted(self, queryset=None):
        """ Get all the projects that are drafted in the queryset.

        :queryset: The queryset in which to search for projects
        :return: A list of in review project objects
        """
        if queryset is None:
            queryset = super(ProjectManager, self).get_queryset()
        drafted_projects = queryset.filter(
            project_status=Project.DRAFTED
        ).order_by('updated_at')
        return drafted_projects

    def get_staged(self, queryset=None):
        """ Get all the projects that are staged in the queryset.

        :queryset: The queryset in which to search for projects
        :return: A list of in review project objects
        """
        if queryset is None:
            queryset = super(ProjectManager, self).get_queryset()
        staged_projects = queryset.filter(
            project_status=Project.STAGED
        ).order_by('updated_at')
        return staged_projects

    def statistics(self, queryset=None):
        """
        Return a revolv.project.stats.KilowattStatsAggregator to
        aggregate statistics about the impact of the given queryset of
        projects.
        """
        if queryset is None:
            queryset = super(ProjectManager, self).get_queryset()
        return KilowattStatsAggregator.from_project_queryset(queryset)

    def owned_projects(self, user_profile):
        """ Get all projects owned by a RevolvUserProfile.

        :user: The user of interest
        :return: A list of projects for which user's RevolvUserProfile
        is the ambassador or creator.
        """
        return Project.objects.filter(Q(ambassadors=user_profile) | Q(created_by_user=user_profile))

    def donated_projects(self, user_profile):
        """
        :return: Projects to which this RevolvUserProfile has donated
        """
        return user_profile.project_set.all()

    def donated_completed_projects(self, user_profile):
        """
        :return: Completed projects to which this RevolvUserProfile has donated
        """
        all_payments = Payment.objects.filter(user=user_profile).distinct('project')
        user_impact = 0
        for payment in all_payments:
            project = payment.project
            if project:
                if project.project_status == 'CO':
                    user_impact = user_impact + project.people_affected
        return user_impact

    def create_from_form(self, form, creator):
        """ Creates project from form and sets created_by_user to a RevolvUserProfile.

        :form: The form
        :creator: The RevolvUserProfile of the creator of the project
        :return: Project created and saved
        """
        project = form.save(commit=False)
        project.created_by_user = creator
        project.save()
        return project

    def get_eligible_projects_for_reinvestment(self, queryset=None):
        """
        :return list(queryset) of eligible project to receive reinvestement
        """
        return self.get_active(queryset).filter(monthly_reinvestment_cap__gt=0.0)

    def get_completed_unpaid_off_projects(self, queryset=None):
        """
        :return list(queryset) of completes project which do monthly repayment.
        """
        return self.get_completed(queryset).filter(is_paid_off=True)


class Project(models.Model):
    """
    Project model. Stores basic metadata, information about the project,
    donations, energy impact, goals, and info about the organization.

    Note about project statuses: there are five kinds of statuses that a
    project can have, and we show projects to different users in different
    ways based on their status.

    When an ambassador or admin first creates a project, it becomes DRAFTED,
    which means that it's a draft and can be edited, but is not in a complete
    state yet (description may need editing, etc). Eventualy the ambassador
    can propose the project for review from the admins, at which time it becomes
    PROPOSED. A proposed project is viewable by admins in their dashboard, as
    well as by the ambassadors that created it.

    When an admin approves a project, it becomes STAGED, which means it is ready
    to go but is not active yet, and as such is not viewable by the public. Staged
    projects are also visible to all admins in their dashboards. When it's time
    for the project to go live and start accepting donations, the admin can mark
    it as ACTIVE, which means it will actually be public and people can donate to
    it. When a project is done, the admin can mark it as COMPLETED, at which point
    it will stop accepting donations and start using repayments.
    """
    ACTIVE = 'AC'
    STAGED = 'ST'
    PROPOSED = 'PR'
    COMPLETED = 'CO'
    DRAFTED = 'DR'
    PROJECT_STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (STAGED, 'Staged'),
        (PROPOSED, 'Proposed'),
        (COMPLETED, 'Completed'),
        (DRAFTED, 'Drafted'),
    )
    LESS_THAN_ONE_DAY_LEFT_STATEMENT = "only hours left"
    NO_DAYS_LEFT_STATEMENT = "deadline reached"

    funding_goal = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        help_text='How much do you aim to raise for this project?'
    )

    subfund_payment = models.CharField(
        default=12,
        max_length=255,
        help_text='The id of the main project you are sub-fundraising for.'
    )

    total_kwh_value = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0,
        blank=True,
        null=True,
        help_text='How much is the total kWH value for 25 years to this project?'
    )
    project_url = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=False,
        help_text='How to show project url for this project?'
    )
    title = models.CharField(
        max_length=255,
        help_text='How would you like to title this project?'
    )
    tagline = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='Select a short tag line that describes this project. (No more than 100 characters.)'
    )
    video_url = models.URLField(
        'Video URL',
        max_length=255,
        blank=True,
        null=True,
        help_text='Link to a Youtube video about the project or community.',
    )
    # power output of array in kilowatts
    impact_power = models.FloatField(
        'Expected Killowatt Output',
        blank=True,
        null=True,
        help_text='What is the expected output in killowatts of the proposed solar array?'
    )
    # solar log graphics url
    solar_url = models.URLField(
        'Solar Log Graphics URL',
        max_length=255,
        blank=True,
        null=True,
        help_text='This can be found by going to http://home.solarlog-web.net/, going to the \
            solar log profile for your site, and clicking on the Graphics sub-page. Copy and paste \
            the URL in the address bar into here.'
    )
    location = models.CharField(
        'Organization Address',
        blank=True,
        null=True,
        max_length=255,
        help_text='What is the address of the organization where the solar panels will be installed?'
    )
    # latitude and longitude of the organization location
    location_latitude = models.DecimalField(
        blank=True,
        null=True,
        max_digits=17,
        decimal_places=14,
        default=0.0
    )
    location_longitude = models.DecimalField(
        blank=True,
        null=True,
        max_digits=17,
        decimal_places=14,
        default=0.0
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    end_date = models.DateField(
        help_text='When will this crowdfunding project end?'
    )
    # the start date of a project is whenever the project becomes live,
    # so we have to set it dynamically. Accordingly, the start_date
    # field is blank=True.
    start_date = models.DateField(
        blank=True,
        null=True
    )
    project_status = models.CharField(
        max_length=2,
        choices=PROJECT_STATUS_CHOICES,
        default=DRAFTED
    )
    cover_photo = ProcessedImageField(
        upload_to='covers/',
        processors=[ResizeToFill(1200, 500)],
        format='JPEG',
        options={'quality': 80},
        default=None,
        help_text='Choose a beautiful high resolution image to represent this project.',
    )

    profile_picture = ProcessedImageField(
        upload_to='covers/',
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 80},
        default='/media/covers/genericprofile.jpg',
        null=True,
        help_text='Choose a beautiful high resolution profile image to represent this project.',
        blank=True,
    )

    preview_photo = ImageSpecField(
        source='cover_photo',
        processors=[ResizeToFill(400, 300)],
        format='JPEG',
        options={'quality': 80},
    )
    org_start_date = models.DateField(
        'Organization Founding Date',
        blank=True,
        null=True,
        help_text='When was the organization being helped established?'
    )

    org_name = models.CharField(
        'Organization Name',
        max_length=255,
        help_text='What is the name of the organization being helped?'
    )

    carbon_avoided =  models.CharField(
        'CO2 Avoided',
        blank=True,
        null=True,
        max_length=255,
        help_text='CO2 avoided for this project - new field'
    )

    dollars_saved = models.CharField(
        'Dollars Saved',
        blank=True,
        null=True,
        max_length=255,
        help_text='Lifetime electricity savings for this project - new field'
    )

    installation_status =  models.CharField(
        'Installation Status',
        blank=True,
        null=True,
        max_length=255,
        help_text='Status of installation for this project - new field'
    )

    installation_date_status =  models.CharField(
        'Installation Date Status',
        blank=True,
        null=True,
        max_length=255,
        help_text='Date of installation for this project - new fields'
    )
    city_state = models.CharField(
        'Project City and State',
        max_length=255,
        blank=True,
        null=True,
        help_text='City and State of the project?'
    )

    financial_product =  models.CharField(
        'Financial product',
        blank=True,
        null=True,
        max_length=255,
        help_text='The type of financial product ( PPA or LEASE ) - new fields'
    )

    people_affected = models.PositiveIntegerField(
        default=0,
        blank=True,
        null=True,
        help_text='How many people will be impacted by this project?'
    )

    mission_statement = models.TextField(
        'Organization Mission',
        blank=True,
        null=True,
        help_text='What is the mission statement of the organization being helped by this project?',
    )

    org_about = models.TextField(
        'Organization Description',
        blank=True,
        null=True,
        help_text='Elaborate more about the organization, what it does, who it serves, etc.'
    )

    description = RichTextField(
        'Project description',
        blank=True,
        null=True,
        help_text='This is the body of content that shows up on the project page.'
    )

    donors = models.ManyToManyField(RevolvUserProfile, blank=True)

    created_by_user = models.ForeignKey(RevolvUserProfile, related_name='created_by_user')

    ambassadors = models.ManyToManyField(RevolvUserProfile, related_name='ambassadors', null=True)

    # energy produced in kilowatt hours
    actual_energy = models.FloatField(default=0.0)
    internal_rate_return = models.DecimalField(
        'Internal Rate of Return',
        max_digits=6,
        decimal_places=3,
        default=0.0,
        help_text='The internal rate of return for this project.'
    )

    # solar data csv files
    daily_solar_data = models.FileField(blank=True, null=True, upload_to="projects/daily/")
    monthly_solar_data = models.FileField(blank=True, null=True, upload_to="projects/monthly/")
    annual_solar_data = models.FileField(blank=True, null=True, upload_to="projects/annual/")

    monthly_reinvestment_cap = models.FloatField(blank=True, default=0.0)
    is_paid_off = models.BooleanField(blank=True, default=False)

    objects = ProjectManager()
    factories = ImportProxy("revolv.project.factories", "ProjectFactories")

    def has_owner(self, creator):
        return self.created_by_user == creator

    def approve_project(self):
        self.project_status = Project.ACTIVE
        if self.start_date is None:
            self.start_date = datetime.date.today()
        self.save()
        return self

    # TODO(noah): change this verbiage. we should probably call the STAGED -> ACTIVE
    # transition "activate_project" and the PROPOSED -> STAGED transition "approve_project"
    # instead.
    def stage_project(self):
        self.project_status = Project.STAGED
        self.save()
        return self

    def unapprove_project(self):
        self.project_status = Project.STAGED
        self.start_date = None
        self.save()
        return self

    def propose_project(self):
        self.project_status = Project.PROPOSED
        self.save()
        return self

    def deny_project(self):
        self.project_status = Project.DRAFTED
        self.save()
        return self

    def complete_project(self):
        self.project_status = Project.COMPLETED
        self.save()
        return self

    def mark_as_incomplete_project(self):
        self.project_status = Project.ACTIVE
        self.save()
        return self

    def update_categories(self, category_list):
        """ Updates the categories list for the project.

        :category_list The list of categories in the submitted form
        """
        # Clears all the existing categories
        self.category_set.clear()

        # Adds the list of categories to the project
        for category in category_list:
            category_object = Category.objects.get(title=category)
            self.category_set.add(category_object)

    def get_absolute_url(self):
        return reverse("project:view", kwargs={"title": str(self.project_url)})

    def get_organic_donations(self):
        return self.payment_set.exclude(user__isnull=True).filter(
            entrant__pk=models.F('user__pk')
        )

    def proportion_donated(self, user):
        """
        :return:
            The proportion that this user has organically donated to this
            project as a float in the range [0, 1] (inclusive)
        """
        user_donation = Payment.objects.donations(
            project=self,
            user=user,
            organic=True
        ).aggregate(
            models.Sum('amount')
        )['amount__sum'] or 0.0
        prop = user_donation / self.amount_donated_organically
        assert 0 <= prop <= 1, "proportion_donated is incorrect!"
        return prop

    def get_anonymous_donors_count(self):
        """
        Total number of anonymous donors count for project
        :return:
        Return anonymous donors count for project
        """
        user_id = User.objects.get(username='Anonymous').pk
        anonymous_user = RevolvUserProfile.objects.get(user_id=user_id)
        return Payment.objects.donations(anonymous_user, self).values("user").count()

    def total_donors(self):
        """
        Total number of donors for the project. This include distinct
        number of donors to project and all anonymous donors for the project
        :return:
            Return total number of donors
        """
        user_id = User.objects.get(username='Anonymous').pk
        anonymous_user = RevolvUserProfile.objects.get(user_id=user_id)

        donor_count = Payment.objects.filter(project=self, admin_reinvestment__isnull=True).exclude(
            user=anonymous_user).values("user").distinct().count()
        anonymous_donors_count = Payment.objects.filter(project=self, user=anonymous_user).values("user").count()

        return donor_count + anonymous_donors_count

    def total_donors_user(self):
        user_id = User.objects.get(username='Anonymous').pk
        anonymous_user = RevolvUserProfile.objects.get(user_id=user_id).id
        payments = Payment.objects.filter(project=self, admin_reinvestment__isnull=True).distinct('user__id')\
            .exclude(user_id=anonymous_user)
        return payments

    @property
    def amount_donated_organically(self):
        """
        :return: the current total amount that has been organically donated to
        this project, as a float.
        """
        return self.get_organic_donations().aggregate(
            models.Sum('amount')
        )["amount__sum"] or 0.0

    @property
    def location_street(self):
        """
        :return: a string of the street name of the location of this project.
        If the project location is malformed, will return an empty string.
        """
        try:
            return self.location.split(',')[0]
        except IndexError:
            return ""

    @property
    def location_city_state_zip(self):
        """
        :return: a string of the city, state, and zip code of the location of this project.
        If the project location is malformed, will return an empty string.
        """
        try:
            pieces = self.location.split(',')
            if len(pieces) >= 3:
                return pieces[1] + "," + pieces[2]
            elif len(pieces) == 2:
                return pieces[1]
            return pieces[0]
        except IndexError:
            return ""

    @property
    def amount_donated(self):
        """
        :return: the current total amount that has been donated to this project,
            as a float.
        """
        return self.payment_set.aggregate(
            models.Sum('amount')
        )["amount__sum"] or 0.0

    @property
    def amount_left(self):
        """
        :return: the current amount of money needed for this project to
            reach its goal, as a float.
        """
        amt_left = float(self.funding_goal) - self.amount_donated
        if amt_left < 0:
            return 0.0
        return amt_left

    @property
    def amount_repaid(self):
        """
        :return: the current amount of money repaid by the project to RE-volv.
        """
        return self.adminrepayment_set.aggregate(models.Sum('amount'))["amount__sum"] or 0.0

    @property
    def total_amount_to_be_repaid(self):
        """
        :return: the total amount of money to be repaid by the project to RE-volv.
        """
        # TODO (https://github.com/calblueprint/revolv/issues/291): Actually
        # calculate this amount based off of interest, but using the project's
        # funding goal is sufficient for now.
        return self.funding_goal

    @property
    def rounded_amount_left(self):
        """
        :return: The amount needed to complete this project, floored to the nearest
            dollar.

        Note: if for some reason the amount left is negative, this will perform a
        ceiling operation instead of a floor, but that should never happen.
        """
        return int(self.amount_left)

    @property
    def partial_completeness(self):
        """
        :return: a float between 0 and 1, representing the completeness of this
            project with respect to its goal (1 if exactly the goal amount, or
            more, has been donated, 0 if nothing has been donated).
        """
        ratio = self.amount_donated / float(self.funding_goal)
        return min(ratio, 1.0)

    @property
    def percent_complete(self):
        """
        :return: a floored int between 0 and 100, representing the completeness of this
            project with respect to its goal (100 if exactly the goal amount, or
            more, has been donated, 0 if nothing has been donated).
        """
        return int(self.partial_completeness * 100)

    def partial_completeness_as_js(self):
        return unicode(self.partial_completeness)

    @property
    def percent_repaid(self):
        """
        :return: a floored int between 0 and 100, representing the amount repaid
        in respect to its repayment goal (100 if exactly the goal amount, or
        more, has been donated, 0 if nothing has been donated).
        """
        return int(self.partial_repayment * 100)

    @property
    def partial_repayment(self):
        """
        :return: a float between 0 and 1, representing the repayment progress
        of this project with respect to the repayment goal (1 if exactly the
        goal amount, or more, has been donated, 0 if nothing has been donated).
        """
        ratio = self.amount_repaid / float(self.total_amount_to_be_repaid)
        return min(ratio, 1.0)

    def partial_repayment_as_js(self):
        return unicode(self.partial_repayment)

    @property
    def total_days(self):
        """
        :return the total length of the campaign of this project,
        or None if the project hasn't started yet.

        Note: if a project's campaign starts and ends on the same day, it is
        defined to be one day long, not zero days long.
        """
        if self.start_date is None:
            return None
        return max((self.end_date - self.start_date).days + 1, 0)

    @property
    def days_until_end(self):
        """
        :return: the difference between today and the end date of this project.
        May be negative.
        """
        return (self.end_date - datetime.date.today()).days

    @property
    def days_so_far(self):
        """
        :return: the integer number of days that have passed since
        this project's campaign began, or None if it has not started
        yet.
        """
        if self.start_date is None:
            return None
        difference = (datetime.date.today() - self.start_date).days
        if difference < 0:
            return 0
        if difference > self.total_days:
            return self.total_days
        return difference

    @property
    def days_left(self):
        """
        :return: the integer number of days until the end of this project,
        or 0 if the project's campaign has finished.
        """
        return max(self.days_until_end, 0)

    def formatted_days_left(self):
        """
        :return: the number of days left in this project's campaign, formatted
        according to how many days left there are. This includes a default message
        when there are 0 days left instead of just saying "0".

        TODO: this should probably be moved to the template logic.
        """
        days_left = self.days_until_end
        if days_left == 1:
            return "1 day left"
        if days_left == 0:
            return self.LESS_THAN_ONE_DAY_LEFT_STATEMENT
        if days_left < 0:
            return self.NO_DAYS_LEFT_STATEMENT
        return unicode(days_left) + " days left"

    @property
    def is_active(self):
        return self.project_status == Project.ACTIVE

    @property
    def is_proposed(self):
        return self.project_status == Project.PROPOSED

    @property
    def is_drafted(self):
        return self.project_status == Project.DRAFTED

    @property
    def is_staged(self):
        return self.project_status == Project.STAGED

    @property
    def is_completed(self):
        return self.project_status == Project.COMPLETED

    @property
    def status_display(self):
        return dict(Project.PROJECT_STATUS_CHOICES)[self.project_status]

    @property
    def categories(self):
        return [category.title for category in self.category_set.all()]

    @property
    def updates(self):
        """
        :return: The set of all ProjectUpdate models associated with this project.
        """
        return self.updates.all()

    @property
    def donation_levels(self):
        """
        :return: The set of all DonationLevel models associated with this project.
        """
        return self.donationlevel_set.all()

    @property
    def statistics(self):
        """
        Return a revolv.project.stats.KilowattStatsAggregator for this project.
        Having this as a property is usefule in templates where we need to display
        statistics about the project (e.g. lbs carbon saved, $ saved, etc).
        """
        return KilowattStatsAggregator.from_project(self)

    def add_update(self, text):
        update = ProjectUpdate(update_text=text, project=self)
        update.save()

    @property
    def reinvest_amount_left(self):
        """
        :return max reinvestment can be receive
        """
        return min(self.amount_left, self.monthly_reinvestment_cap)

    def get_statistic_for_project(self):
        user_impact = 0
        project_funding_total = (int)(self.funding_goal)
        amount_donated = (int)(self.amount_donated)
        project_total_kwh_value = self.total_kwh_value
        total_carbon_avoided = float(project_total_kwh_value) * 1.5
        per_doller_co2_avoided = total_carbon_avoided / project_funding_total
        project_impact = per_doller_co2_avoided * amount_donated
        user_impact += project_impact
        return user_impact

    def paid_off(self):
        """Set the project PAID_OFF flag
        """
        self.is_paid_off = True
        self.save()

    def __unicode__(self):
        return self.title + '-' + self.project_status

class StripeDetails(models.Model):
    stripe_customer_id = models.CharField(max_length=32, blank=True, null=True)
    subscription_id = models.CharField(max_length=32, blank=True, null=True)
    plan = models.CharField(max_length=64, blank=True, null=True)
    stripe_email = models.EmailField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(RevolvUserProfile, related_name='stripe_donor')
    amount = models.FloatField(default=0)
    donation_amount = models.FloatField(default=0)


class AnonymousUserDetail(models.Model):
    email = models.CharField(max_length=254, blank=True, null=True)
    ip_address = models.IPAddressField(blank=True, null=True, default=None)
    amount = models.FloatField(default=0)
    city = models.CharField(max_length=254,blank=True, null=True)
    region_code = models.CharField(max_length=10,blank=True, null=True)
    region_name = models.CharField(max_length=254,blank=True, null=True)
    time_zone = models.CharField(max_length=254,blank=True, null=True)
    country_name = models.CharField(max_length=254,blank=True, null=True)
    zip_code = models.CharField(max_length=30,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class ProjectUpdate(models.Model):
    factories = ImportProxy("revolv.project.factories", "ProjectUpdateFactories")
    update_text = RichTextField(
        'Update content',
        help_text="What should be the content of the update?"
    )

    date = models.DateField(
        'Date of update creation',
        help_text="What time was the update created?",
        auto_now_add=True
    )

    project = models.ForeignKey(
        Project,
        related_name="updates"
    )

    def __unicode__(self):
        return '%s at %s: %s' % (self.project, self.date, self.update_text[:50])


class ProjectMatchingDonors(models.Model):
    """
    Model to track matching donors and there amount.
    """
    project = models.ForeignKey(Project)
    matching_donor = models.ForeignKey(RevolvUserProfile, related_name='matching_donor')
    amount = models.IntegerField()


class Category(models.Model):
    """
    Categories that a project is associated with. Categories are predefined,
    and as of now, loaded through fixtures.
    """
    HEALTH = 'Health'
    ARTS = 'Arts'
    FAITH = 'Faith'
    EDUCATION = 'Education'
    COMMUNITY = 'Community'

    valid_categories = [HEALTH, ARTS, FAITH, EDUCATION, COMMUNITY]

    factories = ImportProxy("revolv.project.factories", "CategoryFactories")

    title = models.CharField(max_length=50, unique=True)
    projects = models.ManyToManyField(Project)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'


class DonationLevel(models.Model):
    """
    Model to track donation levels and perks for projects.
    """
    project = models.ForeignKey(Project)
    description = models.TextField()
    amount = models.IntegerField()

    def __unicode__(self):
        return '%s: %s = %s' % (self.project, self.amount, self.description)


class AnonymousUserDonation(models.Model):
    payment = models.ForeignKey(Payment)
    email = models.CharField(max_length=254, blank=True, null=True)
    ip_address = models.IPAddressField(blank=True, null=True, default=None)
    city = models.CharField(max_length=254, blank=True, null=True)
    region_code = models.CharField(max_length=10, blank=True, null=True)
    region_name = models.CharField(max_length=254, blank=True, null=True)
    time_zone = models.CharField(max_length=254, blank=True, null=True)
    country_name = models.CharField(max_length=254, blank=True, null=True)
    zip_code = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)