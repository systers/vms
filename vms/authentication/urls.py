# Django

from __future__ import unicode_literals
import base64
from django.conf.urls import include,patterns, url
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm,password_reset_complete

from django.core.urlresolvers import reverse
# local Django
from authentication import views
from authentication.views import anonymous_required


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', anonymous_required(login), {'template_name': 'authentication/login.html'}, name='login_process'),
    url(r'^logout/$', logout, {'template_name': 'home/home.html'}, name='logout_process'),
    url(r'^password_reset/$',password_reset,{'post_reset_redirect':'done/'},name='password_reset'),
    url(r'^password_reset/done/$',password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',password_reset_confirm,{'post_reset_redirect':'/authentication/reset/complete/'}, name='password_reset_confirm'), 
    url(r'^reset/complete/$',password_reset_complete,name='password_reset_complete'),
)
