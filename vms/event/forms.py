from django import forms
from django.db import models
from django.forms import ModelForm

from event.models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'name',
            'start_date',
            'end_date',
            'country',
            'state',
            'city',
            'address',
            'venue'
            ]

    def clean(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        event_name = self.cleaned_data.get('name')

        if start_date and end_date:
            if start_date > end_date:
                msg = u"Start date must be before the end date"
                self._errors['start_date'] = self.error_class([msg])

        for event in Event.objects.all():
            if event_name == event.name:
                self._errors['name'] = self.error_class(
                    [u"Another event with same name already exists"])

        return self.cleaned_data


class EventDateForm(forms.Form):
    start_date = forms.DateField(required=True)
    end_date = forms.DateField(required=True)
