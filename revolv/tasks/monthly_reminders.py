from revolv.base.models import RevolvUserProfile
from revolv.lib.mailer import send_revolv_email

from django.conf import settings
from django.core.urlresolvers import reverse
from sesame import utils


def user_reinvestment_reminder():
    """
    Mail worker

    Send email update to user that eligible for reinvestment.
    This should execute after month_allocation

    This how the script do:
    1. Read user profile with reinvest_pool >0 and subscribed_to_repayment_notifications = True
    2. For each user send updated email

    """
    SITE_URL = settings.SITE_URL
    project_reinvest_list_url = SITE_URL + reverse('reinvest_list')
    project_portfolio_url = SITE_URL + reverse('donor:dashboard')
    unsubscribe_update_url = SITE_URL + reverse('unsubscribe', kwargs={'action': 'confirmation'})
    for user in RevolvUserProfile.objects.filter(reinvest_pool__gt=0.0, subscribed_to_repayment_notifications=True):
        data = dict()
        data['amount'] = user.reinvest_pool
        data['portfolio_link'] = project_portfolio_url + utils.get_query_string(user.user)
        data['projects_url'] = project_reinvest_list_url + utils.get_query_string(user.user)
        data['unsubscribe_url'] = unsubscribe_update_url + utils.get_query_string(user.user)
        if user.user.first_name:
            data['first_name'] = user.user.first_name.title()
        else:
            data['first_name'] = 'RE-volv Supporter'

        send_revolv_email(
            'reinvestment_reminder',
            data, [user.user.email]
        )