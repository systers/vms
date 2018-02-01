#Django
from django.conf.urls import url

# local Django
from administrator import views
from administrator.views import GenerateReportView

urlpatterns = [
                       url(r'^report/$', GenerateReportView.as_view(), name='report'),
                       url(r'^settings/$', views.settings, name='settings'),
                       url(r'^profile/(?P<admin_id>\d+)$', views.profile, name='admin_profile'),
                       url(r'^edit/(?P<admin_id>\d+)$', views.edit_profile, name='edit_profile'),
                       ]
