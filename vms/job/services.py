from django.core.exceptions import ObjectDoesNotExist

# vms stuff
from job.models import Job
from shift.services import (
    get_shifts_with_open_slots_for_volunteer, get_unlogged_shifts_by_volunteer_id, get_volunteer_shifts_with_hours
)


def job_not_empty(job_id):
    """ Check if the job exists and is not empty """
    result = True
    job = get_job_by_id(job_id)
    if not job:
        result = False
    return result


def delete_job(job_id):
    """
    Deletes a job if no shifts are associated with it
    """
    result = True
    job = get_job_by_id(job_id)

    if job_not_empty(job_id):
        shifts_in_job = job.shift_set.all()

    if job and (not shifts_in_job):
        job.delete()
    else:
        result = False

    return result


def check_edit_job(job_id, new_start_date, new_end_date):
    """
    Checks if a job can be edited without resulting in invalid shift date
    """

    result = True
    invalid_count = 0
    job = get_job_by_id(job_id)

    if job_not_empty(job_id) and job:

        shifts_in_job = job.shift_set.all()
        # check if there are currently any shifts associated with this job
        if shifts_in_job:
            for shift in shifts_in_job:
                if( shift.date < new_start_date or shift.date > new_end_date):
                    result = False
                    invalid_count += 1

    else:
        result = False

    return {'result' : result, 'invalid_count': invalid_count}


def get_job_by_id(job_id):

    is_valid = True
    result = None

    try:
        job = Job.objects.get(pk=job_id)
    except ObjectDoesNotExist:
        is_valid = False

    if is_valid:
        result = job

    return result


def get_jobs_by_event_id(e_id):
    job_list = Job.objects.filter(event_id=e_id)
    return job_list


def get_jobs_ordered_by_title():
    job_list = Job.objects.all().order_by('name')
    return job_list

def get_signed_up_jobs_for_volunteer(volunteer_id):
    """ Gets sorted list of signed up jobs for a volunteer """

    unsorted_jobs = []
    job_list = []
    shift_list_without_hours = get_unlogged_shifts_by_volunteer_id(volunteer_id)
    shift_list_with_hours = get_volunteer_shifts_with_hours(volunteer_id)

    for shift_with_hours in shift_list_with_hours:
        job_name = str(shift_with_hours.shift.job.name)
        if job_name not in unsorted_jobs:
            unsorted_jobs.append(job_name)
    for shift in shift_list_without_hours:
        job_name = str(shift.job.name)
        if job_name not in unsorted_jobs:
            unsorted_jobs.append(job_name)

    #to sort jobs as per name
    for job in sorted(unsorted_jobs, key=str.lower):
        job_list.append(job)
    return job_list

def remove_empty_jobs_for_volunteer(job_list, volunteer_id):
    """ Removes all jobs from a job list without shifts """
    new_job_list = []
    for job in job_list:
        shift_list = get_shifts_with_open_slots_for_volunteer(job.id, volunteer_id)
        if shift_list:
            new_job_list.append(job)
    return new_job_list
