# Django
from django import forms

# local Django
from volunteer.models import Volunteer
from shift.models import Report

import dns.resolver  #added dnspython in requirements.txt
import re


class ReportForm(forms.Form):
    event_name = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\.)|(,)|(\-)|(!)]+$',
        max_length=75,
        required=False)
    job_name = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)]+$', max_length=75, required=False)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)

    class Meta:
        model = Report


class SearchVolunteerForm(forms.Form):
    first_name = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)|(\-)]+$', max_length=30, required=False)
    last_name = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)|(\-)]+$', max_length=30, required=False)
    city = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)|(\-)]+$', max_length=75, required=False)
    state = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)|(\-)]+$', max_length=75, required=False)
    country = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)|(\-)]+$', max_length=75, required=False)
    organization = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(\s)|(\-)]+$', max_length=75, required=False)
    event = forms.CharField(required=False)
    job = forms.CharField(required=False)

   
class VolunteerForm(forms.ModelForm):
    unlisted_organization = forms.RegexField(
        regex=r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\-)|(:)]+$',
        max_length=100,
        required=False
    )

    class Meta:
        model = Volunteer
        fields = [
            'first_name', 'last_name', 'address',
            'phone_number', 'email', 'websites',
            'description', 'resume', 'resume_file',
            'reminder_days'
        ]

    def check_if_google_email(self):
        gmail_host_pattern = re.compile("(.google.com.|.googlemail.com.|.psmtp.com.)$", re.IGNORECASE)
        data = self.cleaned_data['email']
        test_data = data.slice('@')
        
        if test_data and test_data!=" ":
            host = test_data[-1]
        else:
            return False

        if host == "gmail.com" or host == "googlemail.com" or host == "psmtp.com":
            return True

        else:
            valid_hosts = dns.resolver.query(host, 'MX')
            for host in valid_hosts:
                    try:
                        response = gmail_host_pattern.findall(str(host.exchange))
                        if response and len(response) > 0:
                                return True
                    except:
                        return False    #Invalid Host
                    
        return False

    def check_duplication(self):
        data = self.cleaned_data['email']
        if data.count('@') != 1:     #Invalid Email Alert : Ideally the form should be reloaded and a valid email should be requested
            print("Invalid Email")
            return -1
        elif check_if_google_email(data):
            data_copy = data    # copy of data to prevent unwanted manipulation of original data
            test_data = data_copy.slice('@')
            username = test_data[0]
            if "+" in username:
                accepted_part = username.splice('+')[0]     #Anything after '+' is ignored
            else:
                accepted_part = username
            
            if "." in accepted_part:
                accepted_part.replace('.', '')
            
            test_email = accepted_part + test_data[1]
            
            volunteers = Volunteer.objects.all()
            for volunteer in volunteers:
                if test_email == volunteer.email:
                    print("That Email already exists!")
                    return True     # Duplication Detected : Ideally the form should be reloaded as duplication has to be prevented

        elif check_if_google_email(data) == -1:  #Invalid Email Alert : Ideally the form should be reloaded and a valid email should be requested
            print("Invalid Email")
            return -1

        return False       #All is OK, No duplicate or invalid emails detected. Ideally, entered information should be forwarded ahead.
                  

