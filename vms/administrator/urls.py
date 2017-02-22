from administrator import views
from administrator.views import *
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^report/$', GenerateReportView.as_view(), name='report'),
    url(r'^settings/$', views.settings, name='settings'),
)
