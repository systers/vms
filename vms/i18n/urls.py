from django.conf.urls import patterns, include, url
from django.contrib import admin
from i18n import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^set_language/', views.set_language),
)

