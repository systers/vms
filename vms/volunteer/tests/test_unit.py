# third party

# Django
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.test.testcases import TestCase

# local Django
from pom.pages.basePage import BasePage
from shift.utils import create_volunteer_with_details
from volunteer.models import Volunteer


class VolunteerModelTests(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @staticmethod
    def create_valid_vol():
        vol = [
            'Goku', "Son", "Goku", "Kame House", "East District",
            "East District", "East District", "9999999999", "idonthave@gmail.com"
        ]
        return create_volunteer_with_details(vol)

    @staticmethod
    def create_invalid_vol():
        vol = [
            'Goku~', "Son", "Goku", "Kame House", "East District",
            "East District", "East District", "9999999999", "idonthave@gmail.com"
        ]
        return create_volunteer_with_details(vol)

    def test_valid_model_create(self):
        valid_volunteer = VolunteerModelTests.create_valid_vol()

        # Check DB for volunteer create.
        self.assertEqual(len(Volunteer.objects.all()), 1)

        volunteer_in_db = Volunteer.objects.get(Q(first_name='Son'))
        # Verify correctness.
        self.assertEqual(valid_volunteer.first_name, volunteer_in_db.first_name)
        self.assertEqual(valid_volunteer.last_name, volunteer_in_db.last_name)
        self.assertEqual(valid_volunteer.email, volunteer_in_db.email)
        self.assertEqual(valid_volunteer.phone_number, volunteer_in_db.phone_number)

    def test_invalid_model_create(self):
        invalid_volunteer = VolunteerModelTests.create_invalid_vol()
        self.assertRaisesRegexp(ValidationError, BasePage.FIELD_CANNOT_LEFT_BLANK, invalid_volunteer.full_clean)

    def test_model_edit_with_valid_values(self):
        valid_volunteer = VolunteerModelTests.create_valid_vol()

        # Check DB for volunteer create.
        self.assertEqual(len(Volunteer.objects.all()), 1)

        volunteer_in_db = Volunteer.objects.get(Q(first_name='Son'))
        # Verify correctness.
        self.assertEqual(valid_volunteer.first_name, volunteer_in_db.first_name)
        self.assertEqual(valid_volunteer.last_name, volunteer_in_db.last_name)
        self.assertEqual(valid_volunteer.email, volunteer_in_db.email)
        self.assertEqual(valid_volunteer.phone_number, volunteer_in_db.phone_number)

        valid_volunteer.first_name = 'Prince'
        valid_volunteer.last_name = 'Vegeta'
        valid_volunteer.email = 'iwishihadone@gmail.com'
        valid_volunteer.phone_number = '1234567890'
        valid_volunteer.save()

        # Check single instance
        self.assertEqual(len(Volunteer.objects.all()), 1)

        volunteer_in_db = Volunteer.objects.get(Q(first_name='Prince'))
        # Verify correctness.
        self.assertEqual(valid_volunteer.first_name, volunteer_in_db.first_name)
        self.assertEqual(valid_volunteer.last_name, volunteer_in_db.last_name)
        self.assertEqual(valid_volunteer.email, volunteer_in_db.email)
        self.assertEqual(valid_volunteer.phone_number, volunteer_in_db.phone_number)

    def test_model_edit_with_invalid_values(self):
        valid_volunteer = VolunteerModelTests.create_valid_vol()

        # Check DB for volunteer create.
        self.assertEqual(len(Volunteer.objects.all()), 1)

        volunteer_in_db = Volunteer.objects.get(Q(first_name='Son'))
        # Verify correctness.
        self.assertEqual(valid_volunteer.first_name, volunteer_in_db.first_name)
        self.assertEqual(valid_volunteer.last_name, volunteer_in_db.last_name)
        self.assertEqual(valid_volunteer.email, volunteer_in_db.email)
        self.assertEqual(valid_volunteer.phone_number, volunteer_in_db.phone_number)

        valid_volunteer.first_name = 'Prince'
        valid_volunteer.last_name = 'Vegeta'
        valid_volunteer.email = 'iwishihadone@gmail.com'
        valid_volunteer.phone_number = '1234567890'

        # Check save isn't working.
        self.assertRaisesRegexp(ValidationError, BasePage.FIELD_CANNOT_LEFT_BLANK, valid_volunteer.full_clean)
        # Check single instance
        self.assertEqual(len(Volunteer.objects.all()), 1)

    def test_model_delete(self):
        valid_volunteer = VolunteerModelTests.create_valid_vol()

        # Check DB for volunteer create.
        self.assertEqual(len(Volunteer.objects.all()), 1)

        volunteer_in_db = Volunteer.objects.get(Q(first_name='Son'))
        # Verify correctness.
        self.assertEqual(valid_volunteer.first_name, volunteer_in_db.first_name)
        self.assertEqual(valid_volunteer.last_name, volunteer_in_db.last_name)
        self.assertEqual(valid_volunteer.email, volunteer_in_db.email)
        self.assertEqual(valid_volunteer.phone_number, volunteer_in_db.phone_number)

        volunteer_in_db.delete()

        # Check 0 instance
        self.assertEqual(len(Volunteer.objects.all()), 0)

    def test_model_representation(self):
        valid_volunteer = VolunteerModelTests.create_valid_vol()

        # Check DB for volunteer create.
        self.assertEqual(len(Volunteer.objects.all()), 1)

        volunteer_in_db = Volunteer.objects.get(Q(first_name='Son'))
        # Verify correctness.
        self.assertEqual(valid_volunteer.first_name, volunteer_in_db.first_name)
        self.assertEqual(valid_volunteer.last_name, volunteer_in_db.last_name)
        self.assertEqual(valid_volunteer.email, volunteer_in_db.email)
        self.assertEqual(valid_volunteer.phone_number, volunteer_in_db.phone_number)

        # Check representation
        self.assertEqual(str(volunteer_in_db), 'Son Goku')

