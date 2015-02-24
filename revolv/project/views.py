from decimal import Decimal

from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import FormView
from revolv.base.users import UserDataMixin
from revolv.payments.forms import CreditCardDonationForm
from revolv.payments.services import PaymentService
from revolv.project import forms
from revolv.project.models import Project


class CreateProjectView(CreateView):
    """
    The view to create a new project. Redirects to the homepage upon success.

    Accessed through /project/create
    """
    model = Project
    template_name = 'project/edit_project.html'
    form_class = forms.ProjectForm

    def get_success_url(self):
        return reverse('ambassador:dashboard')

    def form_valid(self, form):
        new_project = Project.objects.create_from_form(form, self.request.user.revolvuserprofile)
        messages.success(self.request, new_project.title + ' has been created!')
        return super(CreateProjectView, self).form_valid(form)

    # sets context to be the create view, doesn't pass in the id
    def get_context_data(self, **kwargs):
        context = super(CreateProjectView, self).get_context_data(**kwargs)
        context['action'] = reverse('project:new')
        context['GOOGLEMAPS_API_KEY'] = settings.GOOGLEMAPS_API_KEY
        return context


class UpdateProjectView(UpdateView):
    """
    The view to update a project. It is the same view as creating a new
    project, though it prepopulates the existing field and passes in the
    project id. Redirects to the project page upon success.

    Accessed through /project/edit/{project_id}
    """
    model = Project
    template_name = 'project/edit_project.html'
    form_class = forms.ProjectForm

    def get_success_url(self):
        messages.success(self.request, 'Project details updated')
        return reverse('project:view', kwargs={'pk': self.get_object().id})

    # sets context to be the edit view by providing in the model id
    def get_context_data(self, **kwargs):
        context = super(UpdateProjectView, self).get_context_data(**kwargs)
        context['action'] = reverse('project:edit',
                                    kwargs={'pk': self.get_object().id})
        return context


class ReviewProjectView(UserDataMixin, UpdateView):
    """
    The view to review a project. Shows the same view as ProjectView, but at
    the top, has a button group through which an ambassador or admin can
    update the project status.

    Accessed through /project/review/{project_id}
    """
    model = Project
    template_name = 'project/review_project.html'
    form_class = forms.ProjectStatusForm

    def get_success_url(self):
        if self.is_administrator:
            return "%s?active_project=%d" % (reverse('administrator:dashboard'), self.get_object().id)
        else:
            return reverse('project:view', kwargs={'pk': self.get_object().id})

    # Checks the post request and updates the project_status
    def form_valid(self, form):
        project = self.object
        if '_approve' in self.request.POST:
            messages.success(self.request, project.title + ' has been approved')
            project.approve_project()
        elif '_propose' in self.request.POST:
            messages.success(self.request, project.title + ' is now pending approval')
            project.propose_project()
        elif '_deny' in self.request.POST:
            messages.info(self.request, project.title + ' has been denied')
            project.deny_project()
        elif '_complete' in self.request.POST:
            messages.success(self.request, project.title + ' has been completed')
            project.complete_project()
        elif '_incomplete' in self.request.POST:
            messages.info(self.request, project.title + ' has been marked as incomplete')
            project.mark_as_incomplete_project()
        elif '_repayment' in self.request.POST:
            repayment_amount = Decimal(self.request.POST['_repayment_amount'])
            PaymentService.create_repayment(self.user_profile, repayment_amount, project)
            messages.success(self.request, '$' + str(repayment_amount) + ' repaid by ' + project.org_name)
        return redirect(self.get_success_url())


class PostFundingUpdateView(UpdateView):
    """
    The view to review a project. Shows the same view as ProjectView, but at
    the top, has a button group through which an ambassador or admin can
    update the project status.

    Accessed through /project/review/{project_id}
    """
    model = Project
    template_name = 'project/post_funding_update.html'
    form_class = forms.PostFundingUpdateForm

    def get_success_url(self):
        return reverse('project:view', kwargs={'pk': self.get_object().id})


class ProjectView(UserDataMixin, FormView):
    """
    The project view. Displays project details and allows for editing.

    Accessed through /project/{project_id}
    """
    model = Project
    template_name = 'project/project.html'
    form_class = CreditCardDonationForm

    # pass in Project and Maps API key
    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['project'] = self.project
        context['GOOGLEMAPS_API_KEY'] = settings.GOOGLEMAPS_API_KEY
        return context

    def dispatch(self, request, *args, **kwargs):
        # always populate self.user, etc
        self.project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        super_response = super(ProjectView, self).dispatch(request, *args, **kwargs)
        if (self.project.is_active or self.project.is_completed or
                (self.user.is_authenticated() and (self.project.has_owner(self.user_profile) or self.is_administrator))):
            return super_response
        else:
            return self.deny_access()

    def form_valid(self, form):
        form.process_payment(self.project, self.user)
        return super(CreateProjectDonationView, self).form_valid(form)

    @property
    def success_url(self):
        return '/project/{0}'.format(self.kwargs.get('pk'))


def validate_payment(request, *args, **kwargs):
    form = CreditCardDonationForm(request.POST)
    errors = form.errors
    confirm = None
    if not errors:
        data = form.data.dict()
        del data['csrfmiddlewaretoken']
        confirm = data
    return JsonResponse({
        'valid': not errors,
        'errors': errors,
        'confirm': confirm,
    })


def submit_payment(request, *args, **kwargs):
    # TODO: actual payment isn't happening, obvi
    form = CreditCardDonationForm(request.POST)
    return JsonResponse({
        'amount': form.data['amount'],
        'success': True
    })


class CreateProjectDonationView(UserDataMixin, FormView):
    model = Project
    template_name = 'project/donate.html'
    form_class = CreditCardDonationForm

    def get_context_data(self, **kwargs):
        context = super(CreateProjectDonationView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.get(pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        project = Project.objects.get(pk=self.kwargs.get('pk'))
        form.process_payment(project, self.user)
        return super(CreateProjectDonationView, self).form_valid(form)

    @property
    def success_url(self):
        return '/project/{0}'.format(self.kwargs.get('pk'))
