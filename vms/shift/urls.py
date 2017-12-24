# Django
from django.urls import path

# local Django
from shift import views
from shift.views import *

app_name='shift'
urlpatterns = [
    path('add_hours/<int:shift_id>/<int:volunteer_id>/', AddHoursView.as_view(), name='add_hours'),
    path('add_hours_manager/<int:shift_id>/<int:volunteer_id>/', AddHoursManagerView.as_view(), name='add_hours_manager'),
    path('create/<int:job_id>/', ShiftCreateView.as_view(), name='create'),
    path('cancel/<int:shift_id>/<int:volunteer_id>/', views.cancel, name='cancel'),
    path('delete/<int:shift_id>/', ShiftDeleteView.as_view(), name='delete'),
    path('clear_hours/<int:shift_id>/<int:volunteer_id>/', ClearHoursView.as_view(), name='clear_hours'),
    path('clear_hours_manager/<int:shift_id>/<int:volunteer_id>/', ClearHoursManager.as_view(), name='clear_hours_manager'),
    path('edit/<int:shift_id>/', ShiftUpdateView.as_view(), name='edit'),
    path('edit_hours/<int:shift_id>/<int:volunteer_id>/', EditHoursView.as_view(), name='edit_hours'),
    path('edit_hours_manager/<int:shift_id>/<int:volunteer_id>/', EditHoursManagerView.as_view(), name='edit_hours_manager'),
    path('list_jobs/', JobListView.as_view(), name='list_jobs'),
    path('list_shifts/<int:job_id>/', ShiftListView.as_view(), name='list_shifts'),
    path('view_shift/<int:shift_id>/', views.view_volunteers, name='view_volunteers'),
    path('list_shifts_sign_up/<int:job_id>/<int:volunteer_id>/', views.list_shifts_sign_up, name='list_shifts_sign_up'),
    path('manage_volunteer_shifts/<int:volunteer_id>/', ManageVolunteerShiftView.as_view(), name='manage_volunteer_shifts'),
    path('sign_up/<int:shift_id>/<int:volunteer_id>/', views.sign_up, name='sign_up'),
    path('view_hours/<int:volunteer_id>/', ViewHoursView.as_view(), name='view_hours'),
    path('view_volunteer_shifts/<int:volunteer_id>/', views.view_volunteer_shifts, name='view_volunteer_shifts'),
    path('volunteer_search/', VolunteerSearchView.as_view(), name='volunteer_search'),
]
