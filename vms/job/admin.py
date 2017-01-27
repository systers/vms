from django.contrib import admin

# vms stuff
from job.models import Job


class JobAdmin(admin.ModelAdmin):
    pass
admin.site.register(Job, JobAdmin)
