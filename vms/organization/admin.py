from django.contrib import admin

# vms stuff
from organization.models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Organization, OrganizationAdmin)
