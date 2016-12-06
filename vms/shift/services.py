import datetime
from datetime import date

from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

# vms stuff
from organization.services import get_organization_by_name, get_organizations_ordered_by_name
from shift.models import Shift, VolunteerShift
from volunteer.models import Volunteer
from volunteer.services import get_all_volunteers, get_volunteer_by_id


def add_shift_hours(v_id, s_id, start_time, end_time):

    volunteer_shift = get_volunteer_shift_by_id(v_id, s_id)

    if volunteer_shift:
        volunteer_shift.start_time = start_time
        volunteer_shift.end_time = end_time
        volunteer_shift.save()
    else:
        raise ObjectDoesNotExist


def calculate_duration(start_time, end_time):

    start_delta = datetime.timedelta(
                                    hours=start_time.hour,
                                    minutes=start_time.minute
                                    )
    end_delta = datetime.timedelta(
                                    hours=end_time.hour,
                                    minutes=end_time.minute
                                    )
    working_hours = (float((end_delta - start_delta).seconds) / 60) / 60
    return working_hours


def calculate_total_report_hours(report_list):

    total_hours = 0

    for report in report_list:
        total_hours += report["duration"]

    return total_hours


def cancel_shift_registration(v_id, s_id):

    if s_id and v_id:
        try:
            shift = Shift.objects.get(pk=s_id)
            obj = VolunteerShift.objects.get(volunteer_id=v_id, shift_id=s_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist
        else:
            # remove volunteer from being signed up for this shift
            obj.delete()
    else:
        raise TypeError


def send_reminder():
    """
    Send reminder email for all shifts and volunteers
    days = 7 - one week reminder
    days = 1 - one day reminder
    A volunteer can specify days in the profile
    !This function should be run on the server once a day!
    """
    notifications_number = 0    
    for volunteer in get_all_volunteers():
        days = volunteer.reminder_days
        if days == 1:
            email_word = " tomorrow."
        else:
            email_word = " in " + str(days) + " days."
        v_id = volunteer.id
        shift_list = get_unlogged_shifts_by_volunteer_id(v_id)
        subject = "The Systers - VMS Volunteer Shift Reminder Mail"
        for shift in shift_list:
            date_shift = shift.date
            days_before_shift = date_shift - date.today()
            if days_before_shift.days == days:
                message = "Dear " + volunteer.first_name + \
                ",\n\nThis is your reminder that you have registered for the " + \
                shift.job.name + " job at the " + shift.job.event.name + \
                " event on " + str(shift.date) + \
                ".\nThe shift you signed up starts" + \
                email_word + \
                "\n\nShift Start Time: " + str(shift.start_time) + \
                "\nShift End Time: " + str(shift.end_time) + \
                "\n\nAddress: " + shift.address + \
                "\nVenue: " + shift.venue + \
                "\nCity: " + shift.city + \
                "\nState: " + shift.state + \
                "\nCountry: " + shift.country + \
                "\n\nThank you for registering!"
                send_mail(
                    subject,
                    message,
                    'noreply@systers.org',
                    [volunteer.email],
                    fail_silently=False
                    )
                notifications_number += 1
                #print(message)
    return notifications_number


def clear_shift_hours(v_id, s_id):

    result = True
    volunteer_shift = get_volunteer_shift_by_id(v_id, s_id)

    if volunteer_shift:
        volunteer_shift.start_time = None
        volunteer_shift.end_time = None
        volunteer_shift.save()
    else:
        result = False

    return result


def delete_shift(s_id):
    """
    Check before deleting:
    does the shift exist?
    is a volunteer signed up for the shift?
    """

    result = True
    shift = get_shift_by_id(s_id)
    num_slots_taken = VolunteerShift.objects.filter(shift_id=s_id).count()

    if shift and num_slots_taken == 0:
        shift.delete()
    else:
        result = False

    return result


def edit_shift_hours(v_id, s_id, start_time, end_time):

    volunteer_shift = get_volunteer_shift_by_id(v_id, s_id)

    if volunteer_shift:
        volunteer_shift.start_time = start_time
        volunteer_shift.end_time = end_time
        volunteer_shift.save()
    else:
        raise ObjectDoesNotExist


def generate_report(volunteer_shift_list):

    report_list = []

    for volunteer_shift in volunteer_shift_list:

        volunteer = volunteer_shift.volunteer
        shift = volunteer_shift.shift
        event = shift.job.event
        job = shift.job

        report = {}
        report["first_name"] = volunteer.first_name
        report["last_name"] = volunteer.last_name
        if volunteer.organization:
            report["organization"] = volunteer.organization.name
        elif volunteer.unlisted_organization:
            report["organization"] = volunteer.unlisted_organization
        else:
            report["organization"] = None
        report["event_name"] = event.name
        report["job_name"] = job.name
        report["date"] = shift.date
        report["logged_start_time"] = volunteer_shift.shift.start_time
        report["logged_end_time"] = volunteer_shift.shift.end_time
        report["duration"] = calculate_duration(
                        volunteer_shift.shift.start_time,
                        volunteer_shift.shift.end_time
                        )

        report_list.append(report)

    return report_list


def get_administrator_report(
                            first_name,
                            last_name,
                            organization,
                            event_name,
                            job_name,
                            start_date,
                            end_date
                            ):

    volunteer_shift_list = get_all_volunteer_shifts_with_hours()

    if first_name:
        volunteer_shift_list = volunteer_shift_list.filter(
            volunteer__first_name__icontains=first_name
            )
    if last_name:
        volunteer_shift_list = volunteer_shift_list.filter(
            volunteer__last_name__icontains=last_name
            )
    if organization:
        organization_obj = get_organization_by_name(organization)
        organization_list = get_organizations_ordered_by_name()
        if organization_obj in organization_list:
            # organization associated with a volunteer can be null
            # therefore exclude from the search query volunteers
            # with no associated organization
            # then filter by organization_name
            volunteer_shift_list = volunteer_shift_list.exclude(
                volunteer__organization__isnull=True).filter(
                volunteer__organization__name__icontains=organization
                )
        else:
            # unlisted_organization associated
            # with a volunteer can be left blank
            # therefore exclude from the search query volunteers
            # with a blank unlisted_organization
            # then filter by the unlisted organization name
            volunteer_shift_list = volunteer_shift_list.exclude(
                volunteer__unlisted_organization__exact='').filter(
                volunteer__unlisted_organization__icontains=organization
                )
    if event_name:
        volunteer_shift_list = volunteer_shift_list.filter(
            shift__job__event__name__icontains=event_name
            )
    if job_name:
        volunteer_shift_list = volunteer_shift_list.filter(
            shift__job__name__icontains=job_name
            )
    if (start_date and end_date):
        volunteer_shift_list = volunteer_shift_list.filter(
            shift__date__gte=start_date,
            shift__date__lte=end_date
            )

    report_list = generate_report(volunteer_shift_list)
    return report_list


def get_all_volunteer_shifts_with_hours():

    volunteer_shift_list = VolunteerShift.objects.all()

    # get shifts that have logged hours only
    volunteer_shift_list = volunteer_shift_list.filter(
        start_time__isnull=False, end_time__isnull=False
        )

    # order by date, start_time and end_time in descending order
    volunteer_shift_list = volunteer_shift_list.order_by(
        '-shift__date', '-start_time', '-end_time'
        )

    return volunteer_shift_list


def get_shift_by_id(shift_id):

    is_valid = True
    result = None

    try:
        shift = Shift.objects.get(pk=shift_id)
    except ObjectDoesNotExist:
        is_valid = False

    if is_valid:
        result = shift

    return result


def get_shifts_by_job_id(j_id):
    shift_list = Shift.objects.filter(job_id=j_id)
    return shift_list


def get_shifts_ordered_by_date(j_id):
    shift_list = Shift.objects.filter(job_id=j_id).order_by('date')
    return shift_list


def get_shift_slots_remaining(s_id):

    shift = get_shift_by_id(s_id)
    num_total_slots = shift.max_volunteers
    num_slots_taken = VolunteerShift.objects.filter(shift_id=s_id).count()
    num_slots_remaining = num_total_slots - num_slots_taken

    return num_slots_remaining


def get_shifts_with_open_slots(j_id):

    shift_list_by_date = get_shifts_ordered_by_date(j_id)
    shift_list = []

    for shift in shift_list_by_date:
        slots_remaining = get_shift_slots_remaining(shift.id)
        if slots_remaining > 0:
            shift_map = {}
            shift_map["id"] = shift.id
            shift_map["date"] = shift.date
            shift_map["start_time"] = shift.start_time
            shift_map["end_time"] = shift.end_time
            shift_map["slots_remaining"] = slots_remaining
            shift_list.append(shift_map)

    return shift_list


def get_shifts_with_open_slots_for_volunteer(j_id, v_id):
    """
    Returns shifts with open slots
    all except those for which the volunteer has signed up.
    """
    shift_list_by_date = get_shifts_ordered_by_date(j_id)
    shift_list = []

    for shift in shift_list_by_date:
        slots_remaining = get_shift_slots_remaining(shift.id)
        if slots_remaining > 0 and not is_signed_up(v_id, shift.id):
            shift_map = {}
            shift_map["id"] = shift.id
            shift_map["date"] = shift.date
            shift_map["start_time"] = shift.start_time
            shift_map["end_time"] = shift.end_time
            shift_map["slots_remaining"] = slots_remaining
            shift_list.append(shift_map)

    return shift_list


def get_unlogged_shifts_by_volunteer_id(v_id):

    # get shifts that the volunteer signed up for and
    # that have not been logged yet (in terms of logged start and end times)
    shift_signed_up_list = Shift.objects.filter(
        volunteershift__volunteer_id=v_id,
        volunteershift__start_time__isnull=True,
        volunteershift__end_time__isnull=True
        )

    # this filtering is buggy when done this way, why?
    # it shows the same shift multiple times if
    # multiple volunteers are signed up for the same shift)
    # shift_signed_up_list = shift_signed_up_list.filter(
    # volunteershift__start_time__isnull=True,
    # volunteershift__end_time__isnull=True)

    # order the list by date in ascending order
    shift_signed_up_list = shift_signed_up_list.order_by('date')

    return shift_signed_up_list


def get_volunteer_report(v_id, event_name, job_name, start_date, end_date):

    volunteer_shift_list = get_volunteer_shifts_with_hours(v_id)

    # filter based on criteria provided
    if event_name:
        volunteer_shift_list = volunteer_shift_list.filter(
            shift__job__event__name__icontains=event_name
            )
    if job_name:
        volunteer_shift_list = volunteer_shift_list.filter(
            shift__job__name__icontains=job_name
            )
    if (start_date and end_date):
        volunteer_shift_list = volunteer_shift_list.filter(
            shift__date__gte=start_date,
            shift__date__lte=end_date
            )

    report_list = generate_report(volunteer_shift_list)
    return report_list


def get_volunteer_shift_by_id(v_id, s_id):

    is_valid = True
    result = None

    try:
        volunteer_shift = VolunteerShift.objects.get(
            volunteer_id=v_id, shift_id=s_id
            )
    except ObjectDoesNotExist:
        is_valid = False

    if is_valid:
        result = volunteer_shift

    return result


def get_volunteer_shifts_with_hours(v_id):

    # get shifts that the volunteer is signed up for
    volunteer_shift_list = VolunteerShift.objects.filter(volunteer_id=v_id)

    # get shifts that have logged hours only
    volunteer_shift_list = volunteer_shift_list.filter(
        start_time__isnull=False, end_time__isnull=False
        )

    # order by date, start_time and end_time in descending order
    volunteer_shift_list = volunteer_shift_list.order_by(
        '-shift__date', '-start_time', '-end_time'
        )

    return volunteer_shift_list

def get_volunteers_by_shift_id(s_id):

    volunteer_list = None

    # get volunteers who have signed up for the shift
    volunteer_list = Volunteer.objects.filter(volunteershift__shift_id=s_id)

    # order by name
    volunteer_list = volunteer_list.order_by(
        'first_name', 'last_name'
        )

    return volunteer_list

def get_logged_volunteers_by_shift_id(s_id):

    logged_volunteer_list = None

    # get volunteers who have signed up for the shift
    logged_volunteer_list = VolunteerShift.objects.filter(shift_id=s_id, start_time__isnull=False, end_time__isnull=False)

    # order by name
    logged_volunteer_list = logged_volunteer_list.order_by(
        'volunteer__first_name','volunteer__last_name'
        )

    return logged_volunteer_list

def is_signed_up(v_id, s_id):

    result = True

    volunteer_shift = get_volunteer_shift_by_id(v_id, s_id)
    if not volunteer_shift:
        result = False

    return result


def register(v_id, s_id):

    result = "IS_VALID"
    ERROR_CODE_ALREADY_SIGNED_UP = "ERROR_CODE_ALREADY_SIGNED_UP"
    ERROR_CODE_NO_SLOTS_REMAINING = "ERROR_CODE_NO_SLOTS_REMAINING"

    # a volunteer must not be allowed to register
    # for a shift that they are already registered for
    signed_up = is_signed_up(v_id, s_id)

    if not signed_up:
        volunteer_obj = get_volunteer_by_id(v_id)
        shift_obj = get_shift_by_id(s_id)
        if volunteer_obj and shift_obj:
            num_slots_remaining = get_shift_slots_remaining(s_id)
            if num_slots_remaining > 0:
                registration_obj = VolunteerShift(
                    volunteer=volunteer_obj, shift=shift_obj
                    )
                registration_obj.save()
            else:
                result = ERROR_CODE_NO_SLOTS_REMAINING
        else:
            raise ObjectDoesNotExist
    else:
        result = ERROR_CODE_ALREADY_SIGNED_UP

    return result
