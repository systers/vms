from django.conf.urls import patterns, include, url
from django.contrib import admin
#from volunteer import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('home.urls', namespace='home')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^administrator/', include('administrator.urls', namespace='administrator')),
    url(r'^authentication/', include('authentication.urls', namespace='authentication')),
    url(r'^event/', include('event.urls', namespace='event')),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^job/', include('job.urls', namespace='job')),
    url(r'^organization/', include('organization.urls', namespace='organization')),
    url(r'^registration/', include('registration.urls', namespace='registration')),
    url(r'^shift/', include('shift.urls', namespace='shift')),
    url(r'^volunteer/', include('volunteer.urls', namespace="volunteer")),
)
#handler404 = 'volunteer.views.not_found'
#handler500 = 'volunteer.views.server_error'
#handler403 = 'volunteer.views.permission_denied'
