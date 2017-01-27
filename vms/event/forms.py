from django import forms
from django.forms import ModelForm

# vms stuff
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
        cleaned_data = super(EventForm, self).clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date > end_date:
                msg = u"Start date must be before the end date"
                self._errors['start_date'] = self.error_class([msg])

        return self.cleaned_data


class EventDateForm(forms.Form):
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
