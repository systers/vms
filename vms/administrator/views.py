# third-party
from braces.views import LoginRequiredMixin

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic import View
from django.views.generic.edit import FormView


# local Django
from organization.services import get_organization_by_id
from administrator.forms import ReportForm
from administrator.models import Administrator
from administrator.utils import admin_required
from event.services import get_events_ordered_by_name
from job.services import get_jobs_ordered_by_title
from shift.services import calculate_total_report_hours, get_administrator_report
from organization.services import get_organizations_ordered_by_name
from administrator.services import get_administrator_by_id
from administrator.forms import AdministratorForm


class AdministratorLoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        admin = hasattr(request.user, 'administrator')
        if not admin:
            return render(request, 'vms/no_admin_rights.html', status=403)
        else:
            return super(AdministratorLoginRequiredMixin, self).dispatch(
                request, *args, **kwargs)


class ShowFormView(AdministratorLoginRequiredMixin, FormView):
    """
    Displays the form
    """
    model = Administrator
    form_class = ReportForm
    template_name = "administrator/report.html"
    event_list = get_events_ordered_by_name()
    job_list = get_jobs_ordered_by_title()
    organization_list = get_organizations_ordered_by_name()

    def get(self, request, *args, **kwargs):
        return render(
            request, 'administrator/report.html', {
                'event_list': self.event_list,
                'organization_list': self.organization_list,
                'job_list': self.job_list
            })


class ShowReportListView(LoginRequiredMixin, AdministratorLoginRequiredMixin,
                         ListView):
    """
    Generate the report using ListView
    """
    template_name = "administrator/report.html"
    organization_list = get_organizations_ordered_by_name()
    event_list = get_events_ordered_by_name()
    job_list = get_jobs_ordered_by_title()

    def post(self, request, *args, **kwargs):
        report_list = get_administrator_report(
            self.request.POST['first_name'],
            self.request.POST['last_name'],
            self.request.POST['organization'],
            self.request.POST['event_name'],
            self.request.POST['job_name'],
            self.request.POST['start_date'],
            self.request.POST['end_date'],
        )
        organization = self.request.POST['organization']
        event_name = self.request.POST['event_name']
        total_hours = calculate_total_report_hours(report_list)
        return render(
            request, 'administrator/report.html', {
                'report_list': report_list,
                'total_hours': total_hours,
                'notification': True,
                'organization_list': self.organization_list,
                'selected_organization': organization,
                'event_list': self.event_list,
                'selected_event': event_name,
                'job_list': self.job_list
            })


class GenerateReportView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = ShowFormView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ShowReportListView.as_view()
        return view(request, *args, **kwargs)


@login_required
@admin_required
def settings(request):
    return HttpResponseRedirect(reverse('event:list'))


@login_required
@admin_required
def profile(request, admin_id):
    admin = Administrator.objects.all().filter(id=admin_id)[0]
    response = {"admin": admin}
    return render(request, "administrator/profile.html", response)


@login_required
@admin_required
def edit_profile(request, admin_id):
    admin = get_administrator_by_id(admin_id)
    organization_list = get_organizations_ordered_by_name()
    if not admin:
        return render(request, 'administrator/404.html')
    else:
        print request.POST
        administrator_form = AdministratorForm(request.POST or None, instance=admin)
        if administrator_form.is_valid():
            admin_to_edit = administrator_form.save(commit=False)
            organization_id = request.POST.get('organization_name')
            organization = get_organization_by_id(organization_id)
            if organization:
                admin_to_edit.organization = organization
            else:
                admin_to_edit.organization = None

            # update the volunteer
            admin_to_edit.save()
            print admin_id
            return redirect(reverse('administrator:admin_profile', args=[admin_id]))
        else:
            print "Form not valid"

        return render(request, 'administrator/edit.html', {"administrator": admin, "organization_list": organization_list,
                                                           "administrator_form": administrator_form})

