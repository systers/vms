# Django
from django.urls import path

# local Django
# from administrator.views import AdministratorSignUpView
# from registration import views
from registration.views import AdministratorSignupView, VolunteerSignupView
app_name='registration'
urlpatterns = [
    path('signup_administrator/', AdministratorSignupView.as_view(), name='signup_administrator'),
    path('signup_volunteer/', VolunteerSignupView.as_view(), name='signup_volunteer'),
]
