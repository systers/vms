# Django
from django.urls import include, path
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('admin/', admin.site.urls),
    path('administrator/', include('administrator.urls', namespace='administrator')),
    path('authentication/', include('authentication.urls', namespace='authentication')),
    path('event/', include('event.urls', namespace='event')),
    path('home/', include('home.urls', namespace='home')),
    path('job/', include('job.urls', namespace='job')),
    path('organization/', include('organization.urls', namespace='organization')),
    path('registration/', include('registration.urls', namespace='registration')),
    path('shift/', include('shift.urls', namespace='shift')),
    path('volunteer/', include('volunteer.urls', namespace="volunteer")),
]
