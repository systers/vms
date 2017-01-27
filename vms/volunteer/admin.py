from django.contrib import admin

# vms stuff
from volunteer.models import Volunteer


class VolunteerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Volunteer, VolunteerAdmin)
