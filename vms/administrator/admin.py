from django.contrib import admin

# vms stuff
from administrator.models import Administrator


class AdministratorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Administrator, AdministratorAdmin)
