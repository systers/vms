#Django
from django.conf.urls import  url

# local Django
from administrator import views
from administrator.views import GenerateReportView

urlpatterns = [
                       url(r'^report/$', GenerateReportView.as_view(), name='report'),
                       url(r'^settings/$', views.settings, name='settings'),
                       ]
