# Django
from django.urls import path
from django.contrib.auth import views as auth_views

# local Django
from authentication import views
from authentication.views import anonymous_required

app_name='authentication'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', anonymous_required(auth_views.login), {'template_name': 'authentication/login.html'}, name='login_process'),
    path('logout/', auth_views.logout, {'template_name': 'home/home.html'}, name='logout_process'),
]
