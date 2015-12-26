from django import forms
from django.forms import ModelForm
from django.forms import ModelChoiceField
from volunteer.models import Volunteer
from cities_light.models import Country
import sys

class CountryChoiceField(ModelChoiceField):    #As mentioned at https://docs.djangoproject.com/en/dev/ref/forms/fields/#django.forms.ModelChoiceField
    def label_from_instance(self, obj):
        if sys.version_info[0]==2:
            return unicode(obj.name)   #python 2
        elif sys.version_info[0]==3:
            return str(obj.name)       #python 3

class ReportForm(forms.Form):
    event_name = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\.)|(,)|(\-)|(!)]+$',
        max_length=75,
        required=False
        )
    job_name = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)]+$',
        max_length=75,
        required=False
        )
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)


class SearchVolunteerForm(forms.Form):
    first_name = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)|(\-)]+$',
        max_length=30,
        required=False
        )
    last_name = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)|(\-)]+$',
        max_length=30,
        required=False
        )
    city = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)|(\-)]+$',
        max_length=75,
        required=False
        )
    state = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)|(\-)]+$',
        max_length=75,
        required=False
        )
    country = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)|(\-)]+$',
        max_length=75,
        required=False
        )
    organization = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)|(\-)]+$',
        max_length=75,
        required=False
        )


class VolunteerForm(ModelForm):
    country = CountryChoiceField(queryset=Country.objects.all(), empty_label=None)   #custom field for from to display name at dropdown

    class Meta:
        model = Volunteer
        fields = [
            'first_name',
            'last_name',
            'address',
            'country',
            'phone_number',
            'unlisted_organization',
            'email',
            'websites',
            'description',
            'resume',
            'resume_file',
            'reminder_days'
            ]
