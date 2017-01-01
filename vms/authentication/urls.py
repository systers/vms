from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from authentication import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_process, name='login_process'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'home/home.html'}, name='logout_process'),
)
