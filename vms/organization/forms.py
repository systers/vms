from django.forms import ModelForm

# vms stuff
from organization.models import Organization


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = ['name']
