from django.conf.urls import patterns, url
from registration import views

urlpatterns = patterns('',
    url(r'^signup_administrator/$', views.signup_administrator, name='signup_administrator'),
    url(r'^signup_volunteer/$', views.signup_volunteer, name='signup_volunteer'),
    url(r'^getstate/(?P<country_id>[0-9]+)/$', views.getstate, name='getstate'),
    url(r'^getcity/(?P<region_id>[0-9]+)/$', views.getcity, name='getcity'),
)
