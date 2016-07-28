from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from organization.forms import OrganizationForm
from organization.services import *
from organization.models import *
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy



class AdministratorLoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        admin = None
        try:
            admin = user.administrator
        except ObjectDoesNotExist:
            pass
        if not admin:
            return render(request, 'vms/no_admin_rights.html')
        else:
            return super(AdministratorLoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class OrganizationCreateView(LoginRequiredMixin, AdministratorLoginRequiredMixin, FormView):
    template_name = 'organization/create.html'
    form_class = OrganizationForm

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('organization:list'))


class OrganizationDeleteView(LoginRequiredMixin, AdministratorLoginRequiredMixin, DeleteView):
    model = Organization
    template_name = 'organization/delete.html'
    success_url = reverse_lazy('organization:list')

    def get_object(self, queryset=None):
        organization_id = self.kwargs['organization_id']
        obj = Organization.objects.get(pk=organization_id)
        return obj


class OrganizationUpdateView(LoginRequiredMixin, AdministratorLoginRequiredMixin, UpdateView):
    model_form = Organization
    template_name = 'organization/edit.html'
    success_url = reverse_lazy('organization:list')

    def get_object(self, queryset=None):
        org_id = self.kwargs['organization_id']
        obj = Organization.objects.get(pk=org_id)
        return obj


class OrganizationListView(LoginRequiredMixin, ListView):
    model_form = Organization
    template_name = "organization/list.html"

    def get_queryset(self):
        organizations = Organization.objects.all()
        return organizations
