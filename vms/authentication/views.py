from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.shortcuts import redirect

# vms stuff
from vms import settings


def index(request):
    return redirect(reverse('authentication:login_process'))


def anonymous_required(func):
    """
    Function for login and logout process using Django's built in auth-views
    """
    def as_view(request, *args, **kwargs):
        redirect_to = kwargs.get('next', settings.LOGIN_REDIRECT_URL )
        if request.user.is_authenticated():
            return redirect(redirect_to)
        response = func(request, *args, **kwargs)
        return response
    return as_view
