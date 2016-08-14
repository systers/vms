from django.contrib.auth import views as auth_views
from django.http.response import HttpResponse
from django.shortcuts import redirect
from ratelimit.decorators import ratelimit
from vms import settings



def index(request):
    return HttpResponse("Hello world")


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


@ratelimit(key='ip', rate='50/m')
def login_process(request):
    if getattr(request, 'limited'):
        # return a HTTP 429 TOO_MANY_REQUESTS if to many login attempts
        errorMessage = "Rate limit for login exceeded, please wait before login again"
        return HttpResponse(errorMessage, status=429)

    return anonymous_required(auth_views.login)(request, {'template_name': 'authentication/login.html'})
