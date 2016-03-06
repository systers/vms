import datetime

from django.utils import formats
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from event.forms import EventForm, EventDateForm
from event.services import *
from event.validate_address import *


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


@login_required
def create(request):
    location = ""
    if is_admin(request):
        if request.method == 'POST':
            form = EventForm(request.POST)
            if form.is_valid() and 'create_event' in request.POST:
                start_date = form.cleaned_data['start_date']
                if start_date < (datetime.date.today() - datetime.timedelta(days=1)):
                    messages.add_message(request, messages.INFO, 'Start date should be today\'s date or later.')
                    return render(request, 'event/create.html', {'form': form, 'location':location,})
                else:
                    form.save()
                    return HttpResponseRedirect(reverse('event:list'))
            elif form.is_valid() and 'show_map' in request.POST:
                area = request.POST.get("address", "") + " " + request.POST.get("city", "") + " " + request.POST.get("state", "") + " " + request.POST.get("country", "")
                location = validate_address(area)         
                return render(request, 'event/create.html', {'form': form, 'location':location,})
            else:
                return render(request, 'event/create.html', {'form': form, 'location':location,})
        else:
            form = EventForm()           
            return render(request, 'event/create.html', {'form': form, 'location':location,})
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
    location = ""
    new_edit = False
    if is_admin(request):
        event = None
        if event_id:
            event = get_event_by_id(event_id)

        if request.method == 'POST':
            form = EventForm(request.POST, instance=event)

            if form.is_valid() and 'edit_event' in request.POST:
                start_date_event = form.cleaned_data['start_date']
                end_date_event = form.cleaned_data['end_date']
                event_edit = check_edit_event(event_id, start_date_event, end_date_event)

                #If there are job date conflicts, do not save event
                if not event_edit['result']:
                    return render(
                        request,
                        'event/edit_error.html',
                        {'count': event_edit['invalid_count'], 'jobs': event_edit['invalid_jobs']}
                        )

                form.save()
                return HttpResponseRedirect(reverse('event:list'))
            elif form.is_valid() and 'show_map' in request.POST:
                area = request.POST.get("address", "") + " " + request.POST.get("city", "") + " " + request.POST.get("state", "") + " " + request.POST.get("country", "")
                location = validate_address(area) 
                return render(request, 'event/edit.html', {'form': form, 'location': location, 'new_edit': new_edit,})
            else:
                return render(request, 'event/edit.html', {'form': form, 'location': location, 'new_edit': new_edit,})
        else:
            event.start_date = formats.date_format(event.start_date, "SHORT_DATE_FORMAT")
            event.end_date = formats.date_format(event.end_date, "SHORT_DATE_FORMAT")
            form = EventForm(instance=event)
            area = event.address + " " + event.city + " " + event.state + " " +  event.country
            location = validate_address(area)
            new_edit = True
            return render(request, 'event/edit.html', {'form': form, 'location': location, 'new_edit': new_edit,})
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
