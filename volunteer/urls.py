from django.conf.urls import patterns, url
from volunteer import views
from volunteer.views import *

urlpatterns = patterns('',
    url(r'^delete_resume/(?P<volunteer_id>\d+)$', views.delete_resume, name='delete_resume'),
    url(r'^download_resume/(?P<volunteer_id>\d+)$', views.download_resume, name='download_resume'),
    url(r'^edit/(?P<volunteer_id>\d+)$', VolunteerUpdateView.as_view(), name='edit'),
    url(r'^profile/(?P<volunteer_id>\d+)$', ProfileView.as_view(), name='profile'),
    url(r'^report/(?P<volunteer_id>\d+)$', GenerateReportView.as_view(), name='report'),
    url(r'^search/$', views.search, name='search'),
)
