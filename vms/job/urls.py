# Django
from django.urls import path

# local Django
from job import views
from job.views import CreateJobView, JobDeleteView, JobDetailView, JobUpdateView, JobListView

app_name='job'
urlpatterns = [
    path('create/', CreateJobView.as_view(), name='create'),
    path('delete/(<int:job_id>/', JobDeleteView.as_view(), name='delete'),
    path('details/<int:job_id>/', JobDetailView.as_view(), name='details'),
    path('edit/<int:job_id>/', JobUpdateView.as_view(), name='edit'),
    path('list/', JobListView.as_view(), name='list'),
    path('list_sign_up/<int:event_id>/<int:volunteer_id>/', views.list_sign_up, name='list_sign_up'),
]
