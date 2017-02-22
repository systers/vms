from administrator.models import Administrator
from django.contrib import admin


class AdministratorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Administrator, AdministratorAdmin)
