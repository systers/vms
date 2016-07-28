from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from job.models import Job
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from django.views.generic import DetailView
from job.forms import JobForm
from job.services import *
from job.models import *
from event.services import *
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator


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


class CreateJobView(LoginRequiredMixin, AdministratorLoginRequiredMixin, FormView, ListView):
    template_name = 'job/create.html'
    form_class = JobForm

    def get_queryset(self):
        events = Event.objects.all()
        return events

    def form_valid(self, form):
        job_id = self.request.POST.get('job_id')
        event_id = self.request.POST.get('event_id')
        event = get_event_by_id(event_id)
        print(event)
        job = get_event_by_id(job_id)
        start_date_event = form.instance.start_date
        end_date_event = form.instance.end_date
        start_date_job=form.cleaned_data.get('start_date')
        end_date_job=form.cleaned_data.get('end_date')
        if(start_date_job>=start_date_event and end_date_job<=end_date_event):
            job = form.save(commit=False)
            if job:
                job.event = event
                form.save(commit=True)
                return HttpResponseRedirect(reverse('job:list'))
            else:
                raise Http404
                return HttpResponseRedirect(reverse('job:list'))
        else:
            messages.add_message(self.request, messages.INFO, 'Job dates should lie within Event dates')
            return render(
            self.request,
            'job/create.html',
            {'form': form, 'event_list': event_list}
            )


class JobDeleteView(LoginRequiredMixin, AdministratorLoginRequiredMixin, DeleteView):
    model_form = Job
    template_name = 'job/delete.html'
    success_url = reverse_lazy('job:list')

    def get_object(self, queryset=None):
        job_id = self.kwargs['job_id']
        obj = Job.objects.get(pk=job_id)
        return obj


class JobDetailView(LoginRequiredMixin, DetailView):
    template_name = 'job/details.html'

    def get_object(self, queryset=None):
        job_id = self.kwargs['job_id']
        obj = Job.objects.get(pk=job_id)
        return obj


class JobUpdateView(LoginRequiredMixin, AdministratorLoginRequiredMixin, UpdateView):
    form_class = JobForm
    template_name = 'job/edit.html'
    success_url = reverse_lazy('job:list')

    def get_context_data(self, **kwargs):
        context = super(JobUpdateView, self).get_context_data(**kwargs)
        context['event_list'] = get_events_ordered_by_name()
        return context

    def get_object(self, queryset=None):
        job_id = self.kwargs['job_id']
        obj = Job.objects.get(pk=job_id)
        return obj


class JobListView(LoginRequiredMixin, ListView):
    model_form = Job
    template_name = "job/list.html"

    def get_queryset(self):
        jobs = Job.objects.all()
        return jobs


@login_required
def list_sign_up(request, event_id, volunteer_id):

    if event_id:
        event = get_event_by_id(event_id)
        if event:
            job_list = get_jobs_by_event_id(event_id)
            job_list = remove_empty_jobs_for_volunteer(job_list, volunteer_id)
            return render(request, 'job/list_sign_up.html', {'event': event, 'job_list': job_list, 'volunteer_id': volunteer_id})
        else:
            raise Http404
    else:
        raise Http404
