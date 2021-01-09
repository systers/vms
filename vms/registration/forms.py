from .utils import check_password_similarity_to_identifiers

# Django
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import CommonPasswordValidator

MODEL_PREFIX = "vol"


class UserForm(forms.ModelForm):
    # password not visible when user types it out
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_password(self):
        password = self.cleaned_data["password"]
        username, first_name, last_name, email = (
            self.cleaned_data["username"],
            self.data.get(f"{MODEL_PREFIX}-first_name"),
            self.data.get(f"{MODEL_PREFIX}-last_name"),
            self.data.get(f"{MODEL_PREFIX}-email"),
        )

        checks = dict()
        # check if it contains a lowercase digit
        checks["lower"] = any(char.islower() for char in password)
        # check if it contains a digit
        checks["digit"] = any(char.isdigit() for char in password)
        # check if its length<=6
        checks["size"] = 6 <= len(password)
        # check if it has special characters
        y = "[~!@#$%^&*()_+{}\":;']+$"
        checks["special"] = set(y).intersection(password)
        checks["contains_space"] = " " not in password
        if all(checks.values()):
            # raises an error if the password is not valid
            self._validate_password(
                password,
                {
                    "username": username,
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                },
            )
            return password
        else:
            raise ValidationError(
                "Password must have at least 6 characters, one "
                "lowercase letter, one "
                "special character and one digit and must not contain space."
            )

    def _validate_password(self, password, identifier_data):
        CommonPasswordValidator().validate(password)
        check_password_similarity_to_identifiers(identifier_data, password)

    class Meta:
        model = User
        fields = ("username", "password")
