# Django
from django.urls import path

# local Django
from organization.views import *

app_name='organization'
urlpatterns = [
    path('create/', OrganizationCreateView.as_view(), name='create'),
    path('delete/<int:organization_id>/', OrganizationDeleteView.as_view(), name='delete'),
    path('edit/<int:organization_id>/', OrganizationUpdateView.as_view(), name='edit'),
    path('list/', OrganizationListView.as_view(), name='list'),
]
