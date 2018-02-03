# Django
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    # password not visible when user types it out
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=25)

    class Meta:
        model = User
        fields = ('username', 'password')
