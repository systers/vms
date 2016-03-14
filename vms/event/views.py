import datetime
from django_countries import countries

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from event.forms import EventForm, EventDateForm
from event.services import *


@login_required
def is_admin(request):
    user = request.user
    admin = None

    try:
        admin = user.administrator
    except ObjectDoesNotExist:
        pass

    # check that an admin is logged in
    if admin is not None:
        return True
    else:
        return False
def getcountries():
    temp=[]
    for i in countries:
        temp.append(i[1])
    return temp

@login_required
def create(request):

    if is_admin(request):
        if request.method == 'POST':
            form = EventForm(request.POST)
            c=getcountries()
            if form.is_valid():
                start_date = form.cleaned_data['start_date']
                if start_date < (datetime.date.today() - datetime.timedelta(days=1)):
                    messages.add_message(request, messages.INFO, 'Start date should be today\'s date or later.')
                    print form
                    return render(request, 'event/create.html', {'form': form, 'countries':c,})
                else:
                    form.save()
                    print form
                    return HttpResponseRedirect(reverse('event:list'))
            else:
                return render(request, 'event/create.html', {'form': form,'countries':c,})
        else:
            form = EventForm()
            c=getcountries()
            return render(request, 'event/create.html', {'form': form,'countries':c,})
    else:
        return render(request, 'vms/no_admin_rights.html')


@login_required
def delete(request, event_id):
    if is_admin(request):
        if request.method == 'POST':
            result = delete_event(event_id)
            if result:
                return HttpResponseRedirect(reverse('event:list'))
            else:
                return render(request, 'event/delete_error.html')
        return render(request, 'event/delete.html', {'event_id': event_id})
    else:
        return render(request, 'vms/no_admin_rights.html')


@login_required
def edit(request, event_id):
    if is_admin(request):
        event = None
        c=getcountries()

        if event_id:
            event = get_event_by_id(event_id)

        if request.method == 'POST':
            form = EventForm(request.POST, instance=event)
            
            if form.is_valid():
                start_date_event = form.cleaned_data['start_date']
                end_date_event = form.cleaned_data['end_date']
                event_edit = check_edit_event(event_id, start_date_event, end_date_event)
                if not event_edit['result']:
                    return render(
                        request,
                        'event/edit_error.html',
                        {'count': event_edit['invalid_count'], 'jobs': event_edit['invalid_jobs']}
                        )
                form.save()
                return HttpResponseRedirect(reverse('event:list'))
            else:
                return render(request, 'event/edit.html', {'form': form, 'countries':c,})
        else:
            form = EventForm(instance=event)
            return render(request, 'event/edit.html', {'form': form, 'countries':c,})
    else:
        return render(request, 'vms/no_admin_rights.html')


@login_required
def list(request):
    event_list = get_events_ordered_by_name()
    return render(request, 'event/list.html', {'event_list': event_list})


@login_required
def list_sign_up(request, volunteer_id):
    if request.method == 'POST':
        form = EventDateForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            
            event_list = get_events_by_date(start_date, end_date)
            event_list = remove_empty_events_for_volunteer(event_list, volunteer_id)
            
            return render(
                request,
                'event/list_sign_up.html',
                {'form' : form, 'event_list': event_list, 'volunteer_id': volunteer_id}
                )
        else:
            event_list = get_events_ordered_by_name()
            event_list = remove_empty_events_for_volunteer(event_list, volunteer_id)
            return render(
                request,
                'event/list_sign_up.html',
                {'event_list': event_list, 'volunteer_id': volunteer_id}
                )
    else:
        event_list = get_events_ordered_by_name()
        event_list = remove_empty_events_for_volunteer(event_list, volunteer_id)
        return render(
            request,
            'event/list_sign_up.html',
            {'event_list': event_list, 'volunteer_id': volunteer_id}
            )
