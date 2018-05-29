# Django
from django.conf.urls import url
from django.contrib.auth import views as auth_views

# local Django
from authentication import views
from authentication.views import anonymous_required

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$',
        anonymous_required(auth_views.login),
        {'template_name': 'authentication/login.html'},
        name='login_process'),
    url(r'^logout/$',
        auth_views.logout, {'template_name': 'home/home.html'},
        name='logout_process'),
    url(r'^password_reset/$',
        auth_views.password_reset, {'post_reset_redirect': 'done/'},
        name='password_reset'),
    url(r'^password_reset/done/$',
        auth_views.password_reset_done,
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'post_reset_redirect': '/authentication/reset/complete/'},
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.password_reset_complete,
        name='password_reset_complete'),
]
