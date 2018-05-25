import csv
import calendar
import time
import json

from django.conf import settings
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from revolv.base.models import RevolvUserProfile
from revolv.base.users import UserDataMixin
from revolv.base.utils import ProjectGroup
from revolv.base.views import BaseStaffDashboardView
from revolv.project.models import Project, ProjectMatchingDonors
from revolv.payments.models import Payment, PaymentType, ProjectMontlyRepaymentConfig

class AdministratorDashboardView(BaseStaffDashboardView):
    """
    Basic view for the Administrator dashboard. Shows the list of projects that this
    ambassador owns. Also, shows drafted projects.
    """
    template_name = 'base/dashboard.html'
    role = "admin"

    def get_context_data(self, **kwargs):
        context = super(AdministratorDashboardView, self).get_context_data(**kwargs)
        context["donated_amount"] = self.request.session.get('amount')
        context["donated_project"] = self.request.session.get('project')
        context["cover_photo"] = self.request.session.get('cover_photo')
        context["url"] = self.request.session.get('url')
        context["social"] = self.request.session.get('social')
        if self.request.session.get('social'):
            del self.request.session['social']
        amount = self.user_profile.reinvest_pool + self.user_profile.solar_seed_fund_pool
        if self.user_profile and amount > 0.0:
            context["reinvestment_amount"] = self.user_profile.reinvest_pool + self.user_profile.solar_seed_fund_pool
        else:
            context["reinvestment_amount"] = 0.0
        context["project_dict"][ProjectGroup('Drafted Projects', "drafted")] = Project.objects.get_drafted()
        return context


class AdministratorEmailView(UserDataMixin, TemplateView):
    """View for the list of newsletter subscribers for the dashboard.
    """
    template_name = 'administrator/email.html'

    def get_context_data(self, **kwargs):
        context = super(AdministratorEmailView, self).get_context_data(**kwargs)

        user_profiles = RevolvUserProfile.objects.get_subscribed_to_newsletter()
        user_emails = list(user_profiles.values_list("user__email", flat=True))

        context['subscribed_user_emails'] = user_emails
        return context


def admin_email_csv_download(request):
    """View for downloading the list of newsletter subscribers as a csv file.
    Accessed via AdministratorEmailView.
    """
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="emails.csv"'

    users_subscribed = RevolvUserProfile.objects.get_subscribed_to_newsletter()
    newsletter_rows = [(u.user.email, u.user.first_name, u.user.last_name, u.user.date_joined) for u in
                       users_subscribed]

    writer = csv.writer(response)
    writer.writerow(['Email', 'FirstName', 'LastName', 'DateJoined'])
    writer.writerows(newsletter_rows)

    return response


class AdminManualPaymentView(UserDataMixin, TemplateView):
    template_name = 'administrator/manual_payment.html'

    def get_context_data(self, **kwargs):
        context = super(AdminManualPaymentView, self).get_context_data(**kwargs)
        context["active_projects"] = Project.objects.get_active()
        return context

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            project_id = request.POST.get("project_id")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            amount = request.POST.get("amount", 0)
            amount = float(amount)

            project = get_object_or_404(Project, pk=project_id)

            if project:
                if first_name and last_name:
                    last_name_part = last_name[0:1] + str(int(time.time() * 1000))[6:13]
                    email = first_name + "." + last_name_part + "@re-volv.org"
                    username = first_name[0:15] + last_name_part
                    password = "revolv123"
                    user = User.objects.create_user(username, email, password, first_name=first_name,
                                                    last_name=last_name)
                    user = user.revolvuserprofile
                else:
                    user_id = User.objects.get(username='Anonymous').pk
                    user = RevolvUserProfile.objects.get(user_id=user_id)

                try:
                    admin = RevolvUserProfile.objects.get(user__username=settings.ADMIN_PAYMENT_USERNAME)
                except RevolvUserProfile.DoesNotExist:
                    admin = user

                payment = Payment.objects.create(
                    user=user,
                    entrant=admin,
                    amount=amount,
                    project=project,
                    tip=None,
                    payment_type=PaymentType.objects.get_check(),
                )

                project_matching_donors = ProjectMatchingDonors.objects.filter(project=project, amount__gt=0)
                if project_matching_donors:
                    for donor in project_matching_donors:
                        if donor.amount > amount:
                            matching_donation = amount
                            donor.amount = donor.amount - amount
                            donor.save()
                        else:
                            matching_donation = donor.amount
                            donor.amount = 0
                            donor.save()

                        Payment.objects.create(
                            user=donor.matching_donor,
                            entrant=donor.matching_donor,
                            amount=matching_donation,
                            project=project,
                            tip=None,
                            payment_type=PaymentType.objects.get_check(),
                        )

            data["success"] = True
            data["message"] = "Saved manual payment successfully."
        except Exception:
            data["success"] = False
            data["message"] = "Error while saving manual payment."

        return JsonResponse(data)


def repayment_config(request):
    draw = request.GET.get('draw')
    project_id = request.GET.get('project_id')
    repayment_config_list = ProjectMontlyRepaymentConfig.objects.filter(project_id=project_id)
    payments = []
    for payment in repayment_config_list:
        payment_details = {}
        payment_details['year'] = payment.starting_year
        payment_details['month'] = payment.starting_month
        payment_details['amount'] = payment.amount
        payments.append(payment_details)

    json_response = {"draw": draw, "recordsTotal": ProjectMontlyRepaymentConfig.objects.all().count(),
                     "recordsFiltered": repayment_config_list.count(), "data": payments}

    return HttpResponse(json.dumps(json_response), content_type='application/json')


class ProjectRepaymentSchedule(UserDataMixin, TemplateView):
    template_name = 'administrator/project_repayment_scheduling.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectRepaymentSchedule, self).get_context_data(**kwargs)
        context['project_list'] = Project.objects.get_completed()
        context['project_repayment_list'] = ProjectMontlyRepaymentConfig.objects.filter(project_id__isnull=False) \
            .order_by('project__id').distinct('project__id')

        return context

    @transaction.atomic
    def post(self, request):
        from datetime import datetime
        from dateutil import relativedelta
        data = {}
        try:
            amount = request.POST.get("amount")
            project_id = request.POST.get("project_id")
            start_date = request.POST.get("start-date")
            project = get_object_or_404(Project, pk=project_id)
            start_year, start_month = start_date.split('-')

            if len(start_year) > 4:
                data["success"] = False
                data["message"] = "Please check the year input."
                return JsonResponse(data)
            starting_date = datetime.strptime(start_date, '%Y-%m')
            start_year = int(start_year)
            start_month = int(start_month)

            if request.POST.get("end-date"):
                end_date = request.POST.get("end-date")
                ending_date = datetime.strptime(end_date, '%Y-%m')
                relative_date = relativedelta.relativedelta(ending_date, starting_date)
                total_months = ((relative_date.years * 12) + relative_date.months) + 1
                end_year, end_month = end_date.split('-')
                end_year = int(end_year)
                end_month = int(end_month)

                if end_year == start_year and end_month <= start_month:
                    data["success"] = False
                    data["message"] = "End month cannot be prior or same as starting month."
                    return JsonResponse(data)

                if end_year < start_year or len(str(end_year)) > 4:
                    data["success"] = False
                    data["message"] = "Please check the end year input."
                    return JsonResponse(data)
            else:
                total_months = 12
                end_date = False
            if project:
                update_entry = ProjectMontlyRepaymentConfig.objects.filter(
                    project=project, repayment_type='SSF', starting_year=start_year,
                    starting_month=calendar.month_name[start_month])
                filtered_list = []
                if end_date:
                    initial_month = start_month
                    initial_year = start_year
                    for i in range(0, total_months, 1):
                        exists_entry = ProjectMontlyRepaymentConfig.objects.filter(
                            project=project, repayment_type='SSF', starting_year=initial_year,
                            starting_month=calendar.month_name[initial_month])
                        filtered_list.append(exists_entry)
                        initial_month += 1
                        if initial_month > 12:
                            initial_month = 1
                            initial_year += 1
                    if len(filtered_list) > 0:
                        for month in range(0, total_months, 1):
                            filter_entry = ProjectMontlyRepaymentConfig.objects.filter(
                                project=project, repayment_type='SSF', starting_year=start_year,
                                starting_month=calendar.month_name[start_month])
                            if filter_entry:
                                filter_entry.update(amount=amount)
                            else:
                                ProjectMontlyRepaymentConfig.objects.create(
                                    project=project,
                                    repayment_type='SSF',
                                    starting_year=start_year,
                                    starting_month=calendar.month_name[start_month],
                                    amount=amount,
                                )
                            start_month += 1
                            if start_month > 12:
                                start_month = 1
                                start_year += 1
                elif update_entry:
                    update_entry.update(amount=amount)
                else:
                    for i in range(0, total_months, 1):
                        ProjectMontlyRepaymentConfig.objects.create(
                            project=project,
                            repayment_type='SSF',
                            starting_year=start_year,
                            starting_month=calendar.month_name[start_month],
                            amount=amount,
                        )
                        start_month += 1
                        if start_month > 12:
                            start_month = 1
                            start_year += 1

            data["success"] = True
            data["message"] = "Repayment scheduled successfully"
        except Exception:
            data["success"] = False
            data["message"] = "Error while saving repayment scheduling."
        return JsonResponse(data)
