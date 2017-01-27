from functools import wraps
from django.shortcuts import render
from django.http import Http404
from volunteer.services import get_volunteer_by_id

def vol_id_check(func):
    @wraps(func)
    def wrapped_view(request, volunteer_id):
        vol = getattr(request.user, 'volunteer', hasattr(request.user, 'administrator'))
        if not vol:
            return render(request, 'vms/no_volunteer_access.html', status=403)
        elif vol != True:
            volunteer = get_volunteer_by_id(volunteer_id)
            if not volunteer:
                return render(request, 'vms/no_volunteer_access.html', status=403)
            if not int(volunteer.id) == vol.id:
                return render(request, 'vms/no_volunteer_access.html', status=403)
        return func(request, volunteer_id=volunteer_id)
    return wrapped_view
