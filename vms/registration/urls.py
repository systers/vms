# Django
from django.conf.urls import url

# local Django
# from administrator.views import AdministratorSignUpView
# from registration import views
from registration.views import AdministratorSignupView, VolunteerSignupView, load_cities

urlpatterns = [
    url(r'^signup_administrator/$',
        AdministratorSignupView.as_view(),
        name='signup_administrator'),
    url(r'^signup_volunteer/$',
        VolunteerSignupView.as_view(),
        name='signup_volunteer'),
    url(r'^load_cities/$', load_cities, name='load_cities'),
]

