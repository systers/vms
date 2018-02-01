# Django
from django.conf.urls import url

# local Django
from registration.views import *

urlpatterns = [
    url(r'^signup_administrator/$', AdministratorSignupView.as_view(), name='signup_administrator'),
    url(r'^signup_volunteer/$', VolunteerSignupView.as_view(), name='signup_volunteer'),
]
