#Django
from django.conf.urls import patterns, url

# local Django
from vms.administrator import views
from vms.administrator.views import *

urlpatterns = patterns(
    '',
    url(r'^report/$', GenerateReportView.as_view(), name='report'),
    url(r'^settings/$', views.settings, name='settings'),
)
