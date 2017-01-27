from django.conf.urls import patterns, url

# vms stuff
from shift import views
from shift.views import (
    AddHoursManagerView, AddHoursView, ClearHoursManager, ClearHoursView, EditHoursManagerView, EditHoursView,
    JobListView, ManageVolunteerShiftView, ShiftCreateView, ShiftDeleteView, ShiftListView, ShiftUpdateView,
    ViewHoursView, VolunteerSearchView
)

urlpatterns = patterns('',
    url(r'^add_hours/(?P<shift_id>\d+)/(?P<volunteer_id>\d+)$', AddHoursView.as_view(), name='add_hours'),
    url(r'^add_hours_manager/(?P<shift_id>\d+)/(?P<volunteer_id>\d+)$', AddHoursManagerView.as_view(), name='add_hours_manager'),
    url(r'^create/(?P<job_id>\d+)$', ShiftCreateView.as_view(), name='create'),
    url(r'^cancel/(?P<shift_id>\d+)/(?P<volunteer_id>\d+)$', views.cancel, name='cancel'),
    url(r'^delete/(?P<shift_id>\d+)$', ShiftDeleteView.as_view(), name='delete'),
    url(r'^clear_hours/(?P<shift_id>\d+)/(?P<volunteer_id>\d+)$', ClearHoursView.as_view(), name='clear_hours'),
    url(r'^clear_hours_manager/(?P<shift_id>\d+)/(?P<volunteer_id>\d+)$', ClearHoursManager.as_view(), name='clear_hours_manager'),
    url(r'^edit/(?P<shift_id>\d+)$', ShiftUpdateView.as_view(), name='edit'),
    url(r'^edit_hours/(?P<shift_id>\d+)/(?P<volunteer_id>\d+)$', EditHoursView.as_view(), name='edit_hours'),
    url(r'^edit_hours_manager/(?P<shift_id>\d+)/(?P<volunteer_id>\d+)$', EditHoursManagerView.as_view(), name='edit_hours_manager'),
    url(r'^list_jobs/$', JobListView.as_view(), name='list_jobs'),
    url(r'^list_shifts/(?P<job_id>\d+)$', ShiftListView.as_view(), name='list_shifts'),
    url(r'^view_shift/(?P<shift_id>\d+)$', views.view_volunteers, name='view_volunteers'),
    url(r'^list_shifts_sign_up/(?P<job_id>\d+)/(?P<volunteer_id>\d+)$', views.list_shifts_sign_up, name='list_shifts_sign_up'),
    url(r'^manage_volunteer_shifts/(?P<volunteer_id>\d+)$', ManageVolunteerShiftView.as_view(), name='manage_volunteer_shifts'),
    url(r'^sign_up/(?P<shift_id>\d+)/(?P<volunteer_id>\d+)$', views.sign_up, name='sign_up'),
    url(r'^view_hours/(?P<volunteer_id>\d+)$', ViewHoursView.as_view(), name='view_hours'),
    url(r'^view_volunteer_shifts/(?P<volunteer_id>\d+)$', views.view_volunteer_shifts, name='view_volunteer_shifts'),
    url(r'^volunteer_search/$', VolunteerSearchView.as_view(), name='volunteer_search'),
)
