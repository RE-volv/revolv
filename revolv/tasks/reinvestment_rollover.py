import datetime
from django.conf import settings

from revolv.project.models import Project, ProjectMatchingDonors
from revolv.payments.models import ProjectMontlyRepaymentConfig, AdminReinvestment, PaymentType, Payment, SolarSeedFund
from revolv.base.models import RevolvUserProfile
from django.db.models import Sum
from django.db.models import Q
from revolv.tasks.sfdc import send_donation_info

from celery.task import task

import sys
import time
import logging

logger = logging.getLogger("revolv")


@task
def distribute_reinvestment_fund():
    """
    This task is for Automatic reinvestment

    This is how this script do:
    1. Get all project that is eligible for reinvestment:
        (project with monthly_reinvestment_cap >0 and not fully funded)
    2. For each project determine how we'll reinvest
    3. Add AdminReinvestment object with above value
    4. Reinvestment every user's reinvestment amount in project funding proportion.
    """

    today = datetime.datetime.today()
    if today.day == settings.ADMIN_REINVESTMENT_DATE['day']:
        time.sleep(60)
        ADMIN_PAYMENT_USERNAME = settings.ADMIN_PAYMENT_USERNAME

        try:
            admin = RevolvUserProfile.objects.get(user__username=ADMIN_PAYMENT_USERNAME)
        except RevolvUserProfile.DoesNotExist:
            logger.error("Can't find admin user: {0}. System exiting!".format(ADMIN_PAYMENT_USERNAME))
            sys.exit()

        total_funding_goal = Project.objects.get_active().aggregate(total=Sum('funding_goal'))['total']
        pending_reinvestors = []

        users = RevolvUserProfile.objects.filter(Q(reinvest_pool__gt=0.0) | Q(solar_seed_fund_pool__gt=0.0))
        for user in users:
            reinvest_pool=user.reinvest_pool
            solar_seed_fund_pool = user.solar_seed_fund_pool
            pending_reinvestors.append((user, reinvest_pool, solar_seed_fund_pool))

        for project in Project.objects.get_active():
            reinvest_amount_praportion = float(project.funding_goal)/float(total_funding_goal)

            for (user, reinvest_pool, solar_seed_fund_pool) in pending_reinvestors:
                if solar_seed_fund_pool > 0.0:
                    amount = solar_seed_fund_pool * float("{0:.2f}".format(reinvest_amount_praportion))
                    solar_seed_monthly = SolarSeedFund.objects.create(
                        amount=amount,
                        user=user,
                        project=project
                    )
                    logger.info('Trying to donate %s in %s project!', format(round(amount, 2)), project.title)
                    monthly_seed_fund = Payment(user=user,
                                                project=project,
                                                entrant=user,
                                                payment_type=PaymentType.objects.get_stripe(),
                                                solar_seed_monthly=solar_seed_monthly,
                                                amount=format(round(amount, 2))
                                                )
                    monthly_seed_fund.save()
                    #send_donation_info(user.get_full_name(), round(amount, 2), user.user.email, project.title,
                    #                   address='')
                    user.solar_seed_fund_pool = user.solar_seed_fund_pool - amount
                    user.save()

                if reinvest_pool > 0.0:
                    amount = reinvest_pool * float("{0:.2f}".format(reinvest_amount_praportion))
                    adminReinvestment = AdminReinvestment.objects.create(
                        amount=amount,
                        admin=admin,
                        project=project
                    )
                    logger.info('Trying to reinvest %s in %s project!',format(round(amount,2)),project.title)
                    reinvestment = Payment(user=user,
                                           project=project,
                                           entrant=admin,
                                           payment_type=PaymentType.objects.get_reinvestment_fragment(),
                                           admin_reinvestment=adminReinvestment,
                                           amount=format(round(amount,2))
                                           )

                    reinvestment.save()

                    project_matching_donors = ProjectMatchingDonors.objects.filter(project=project, amount__gt=0)

                    if project_matching_donors:
                        for donor in project_matching_donors:
                            if donor.amount > float(amount):
                                matching_donation = amount
                                donor.amount = donor.amount - amount
                                donor.save()
                            else:
                                matching_donation = donor.amount
                                donor.amount = 0
                                donor.save()

                            tip = None

                            Payment.objects.create(
                                user=donor.matching_donor,
                                entrant=donor.matching_donor,
                                amount=matching_donation,
                                project=project,
                                tip=tip,
                                payment_type=PaymentType.objects.get_stripe(),
                            )

                if project.amount_donated >= project.funding_goal:
                    project.project_status = project.COMPLETED
                    project.save()


        for user in users:
            if user.solar_seed_fund_pool <= 0.01:
                user.solar_seed_fund_pool = 0

            if user.reinvest_pool <= 0.01:
                user.reinvest_pool = 0

            user.save()