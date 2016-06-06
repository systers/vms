from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
#from importlib._bootstrap import _NamespaceLoader
from vms.views import anonymous_required
from django.contrib.auth.decorators import login_required
import registration.views as views
from django.contrib.auth import views as auth_views

#admin.autodiscover()

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
    url(r'^portal', TemplateView.as_view(template_name='home/home.html'),name='home'),
    url(r'^login/$',
         anonymous_required(auth_views.login),
        {'template_name': 'authentication/login.html'},
        name='login_process'),
    url(r'^user/logout/$',
        auth_views.logout,
        {'template_name': 'home/home.html'},
        name='logout_process'),
)
