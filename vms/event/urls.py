# Django
from django.urls import path

# local Django
from event import views
from event.views import EventCreateView, EventDeleteView, EventUpdateView, EventListView
app_name='event'
urlpatterns = [
    path('create/', EventCreateView.as_view(), name='create'),
    path('delete/<int:event_id>/', EventDeleteView.as_view(), name='delete'),
    path('edit/<int:event_id>/', EventUpdateView.as_view(), name='edit'),
    path('list/', EventListView.as_view(), name='list'),
    path('list_sign_up/<int:volunteer_id>/', views.list_sign_up, name='list_sign_up'),
]
