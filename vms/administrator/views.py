# third-party
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin

# Django
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic.edit import FormView, UpdateView

# local Django
from administrator.forms import ReportForm
from administrator.models import Administrator
from administrator.utils import admin_required
from event.services import *
from job.services import *
from shift.services import *


class AdministratorLoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        admin = hasattr(request.user, 'administrator')
        if not admin:
            return render(request, 'vms/no_admin_rights.html', status=403)
        else:
            return super(AdministratorLoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class ShowFormView(AdministratorLoginRequiredMixin, FormView):
    """
    Displays the form
    """
    model = Administrator
    form_class = ReportForm
    template_name = "administrator/report.html"

    def get_context_data(self, **kwargs):
        context = super(ShowFormView, self).get_context_data(
            **kwargs
        )
        context['event_list'] = get_events_ordered_by_name()
        context['job_list'] = get_jobs_ordered_by_title()
        context['organization_list'] = get_organizations_ordered_by_name()
        return context


class ShowReportListView(
    LoginRequiredMixin, AdministratorLoginRequiredMixin, TemplateView
):
    """
    Generate the report using ListView
    """
    template_name = "administrator/report.html"

    def post(self, request, *args, **kwargs):
        report_list = get_administrator_report(
            self.request.POST['first_name'],
            self.request.POST['last_name'],
            self.request.POST['organization'],
            int(self.request.POST['event_id']),
            int(self.request.POST['job_id']),
            self.request.POST['start_date'],
            self.request.POST['end_date'],
        )
        selected_organization = self.request.POST['organization']
        selected_event_id = int(self.request.POST['event_id'])
        selected_job_id = int(self.request.POST['job_id'])

        total_hours = calculate_total_report_hours(report_list)
        return render(
            request, 'administrator/report.html',
            {
                'report_list': report_list, 'total_hours': total_hours,
                'notification': True,
                'selected_organization': selected_organization,
                'selected_event': selected_event_id,
                'selected_job': selected_job_id,
                'event_list': get_events_ordered_by_name(),
                'job_list': get_jobs_ordered_by_title(),
                'organization_list': get_organizations_ordered_by_name()
            }
        )


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
