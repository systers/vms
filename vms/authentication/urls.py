from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

# vms stuff
from authentication import views
from authentication.views import anonymous_required

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', anonymous_required(auth_views.login), {'template_name': 'authentication/login.html'}, name='login_process'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'home/home.html'}, name='logout_process'),
)
