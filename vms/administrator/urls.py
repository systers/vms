from django.conf.urls import patterns, url

# vms stuff
from administrator import views
from administrator.views import GenerateReportView

urlpatterns = patterns('',
    url(r'^report/$', GenerateReportView.as_view(), name='report'),
    url(r'^settings/$', views.settings, name='settings'),
)
