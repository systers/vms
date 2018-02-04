# Django
from django.urls import path

# local Django
from volunteer import views
from volunteer.views import VolunteerUpdateView, ProfileView, GenerateReportView

app_name='volunteer'
urlpatterns = [
    path('delete_resume/<int:volunteer_id>/', views.delete_resume, name='delete_resume'),
    path('download_resume/<int:volunteer_id>/', views.download_resume, name='download_resume'),
    path('edit/<int:volunteer_id>/', VolunteerUpdateView.as_view(), name='edit'),
    path('profile/<int:volunteer_id>/', ProfileView.as_view(), name='profile'),
    path('report/<int:volunteer_id>/', GenerateReportView.as_view(), name='report'),
    path('search/', views.search, name='search'),
]
