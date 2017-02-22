import phonenumbers
from cities_light.models import Country
from django.contrib.auth.models import User
from django.test import TestCase
from registration.phone_validate import validate_phone


# Create your tests here.
class Tests_phone(unittest.TestCase):
