from django.contrib import admin

# vms stuff
from shift.models import Shift, VolunteerShift


class ShiftAdmin(admin.ModelAdmin):
    pass
admin.site.register(Shift, ShiftAdmin)


class VolunteerShiftAdmin(admin.ModelAdmin):
    pass
admin.site.register(VolunteerShift, VolunteerShiftAdmin)
