from django.contrib import admin

# vms stuff
from event.models import Event


class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Event, EventAdmin)
