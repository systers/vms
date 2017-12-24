#Django
from django.urls import path

# local Django
from administrator import views
from administrator.views import GenerateReportView

app_name='administrator'
urlpatterns = [
                       path('report/', GenerateReportView.as_view(), name='report'),
                       path('settings/', views.settings, name='settings'),
                       ]
