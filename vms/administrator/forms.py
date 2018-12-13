from django import forms
from administrator.models import Administrator


class AdministratorForm(forms.ModelForm):
    unlisted_organization = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\-)|(:)]+$',
        max_length=100,
        required=False
    )

    class Meta:
        model = Administrator
        fields = [
            'first_name', 'last_name', 'address',
            'phone_number', 'email'
        ]

    def clean_email(self):
        data = self.cleaned_data['email']
        data_unchanged = data
        if "gmail.com" or "googlemail.com" in data:
            data = data[:-4]
            if "." in data:
                data = data.replace(".", "")
            data = data + '.com'
            if "googlemail.com" in data:
                data = data.replace("@googlemail", "@gmail")
            if '+' in data:
                i = data.find('+')
                j = data.find('@')
                data = data[:i] + data[j:]
            return data
        return data_unchanged


class ReportForm(forms.Form):
    first_name = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)]+$', max_length=30, required=False)
    last_name = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)]+$', max_length=30, required=False)
    organization = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)]+$', max_length=75, required=False)
    event_name = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\.)|(,)|(\-)|(!)]+$',
        max_length=75,
        required=False)
    job_name = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)]+$', max_length=75, required=False)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)

