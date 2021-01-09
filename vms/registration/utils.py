# standard library
from functools import wraps
import re
from difflib import SequenceMatcher

# Django
from django.shortcuts import render
from django.core.exceptions import ValidationError

SIGNUP_IDENTIFIER_ATTRS = ("username", "first_name", "last_name", "email")


def volunteer_denied(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if not hasattr(request.user, "administrator"):
                return render(request, "vms/no_admin_rights.html", status=403)
        return func(request, *args, **kwargs)

    return wrapper


# account can only be created if both passwords match
def match_password(password1, password2):
    return password1 == password2


# check if password is similar to any of the identifer data (username,
# first name of the user....)
def check_password_similarity_to_identifiers(
    identifier_data, password, max_similarity=0.7
):
    """
    Check if the user's password is similar to any of the
    provided user's identification params (first name, username...)
    :param identifier_data: dict with the following structure
    Based on: 'django.contrib.auth.password_validation.
     UserAttributeSimilarityValidator'
    {
        first_name:"string",
        last_name:"string",
        username:"string",
        email: "string"
    }
    :param password: "user password"
    :param max_similarity: similairty coefficeint, default=0.7
    :return: raises a ValidationError if password is similar to any of
    the params from the identifier_data
    """
    for attribute_name in SIGNUP_IDENTIFIER_ATTRS:
        value = identifier_data.get(attribute_name)
        if not value or not isinstance(value, str):
            continue
        value_parts = re.split(r"\W+", value) + [value]
        for value_part in value_parts:
            if (SequenceMatcher(a=password.lower(), b=value_part.lower())
                    .quick_ratio() >= max_similarity):
                raise ValidationError(
                    f"The password is too similar to the {attribute_name}."
                )
