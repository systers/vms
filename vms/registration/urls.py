from django.conf.urls import patterns, url

# vms stuff
from registration.views import AdministratorSignupView, VolunteerSignupView

urlpatterns = patterns('',
    url(r'^signup_administrator/$', AdministratorSignupView.as_view(), name='signup_administrator'),
    url(r'^signup_volunteer/$', VolunteerSignupView.as_view(), name='signup_volunteer'),
)
