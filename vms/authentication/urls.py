# Django
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

# local Django
from authentication import views
from authentication.views import anonymous_required

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$',
        anonymous_required(LoginView.as_view(
        template_name='authentication/login.html')),
        name='login_process'),
    url(r'^logout/$',
        LogoutView.as_view(template_name='home/home.html'),
        name='logout_process'),
    url(r'^change-password/$',
        auth_views.password_change, {'post_change_redirect': 'done/'},
        name='password_change'),
    url(r'^change-password/done/$',
        auth_views.password_change_done,
        name='password_change_done'),
]
