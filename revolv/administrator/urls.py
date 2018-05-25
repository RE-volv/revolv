from django.conf.urls import patterns, url

from revolv.administrator.views import (admin_email_csv_download,
                                        AdministratorDashboardView,
                                        AdministratorEmailView,
                                        AdminManualPaymentView, ProjectRepaymentSchedule)
from revolv.base.users import is_administrator

urlpatterns = patterns(
    '',
    url(r'^$', is_administrator(AdministratorDashboardView.as_view()), name='dashboard'),
    url(r'^email$', is_administrator(AdministratorEmailView.as_view()), name='email'),
    url(r'^email/csv$', admin_email_csv_download, name='emailcsv'),
    url(r'^manualpayment$', is_administrator(AdminManualPaymentView.as_view()), name='manualpayment'),
    url(r'^repayment-schedule$', is_administrator(ProjectRepaymentSchedule.as_view()), name='repayment_schedule'),
)
