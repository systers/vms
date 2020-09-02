# Django
from django.urls import reverse
from django.shortcuts import redirect
from social_django.models import UserSocialAuth

# local Django
from vms import settings


def index(request):
    return redirect(reverse('authentication:login_process'))


def anonymous_required(func):
    """
    Function for login and logout process using Django's built in auth-views
    """

    def as_view(request, *args, **kwargs):
        redirect_to = kwargs.get('next', settings.LOGIN_REDIRECT_URL)
        if request.user.is_authenticated:
            return redirect(redirect_to)
        response = func(request, *args, **kwargs)
        return response

    return as_view

def github_auth_dialog_step(strategy, backend, request, details, *args, **kwargs):
    print(details)
    print(kwargs)
