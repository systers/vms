# third party

# Django
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models import Q
from django.test.testcases import TestCase

# local Django
from organization.models import Organization
from pom.pages.basePage import BasePage
from shift.utils import create_organization_with_details


class OrganizationModelTests(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_valid_organization_create(self):
        # Create Organization
        org = create_organization_with_details('DummyOrg')

        # Check database for org creation
        self.assertEqual(len(Organization.objects.all()), 1)

        org_in_db = Organization.objects.get(Q(name='DummyOrg'))
        # Verify correct name saved
        self.assertEqual(org_in_db.name, org.name)

    def test_invalid_organization_create(self):
        # Create Organization
        org = create_organization_with_details('Dummy~Org')

        # Check if correct error is raised.
        error_message = BasePage.ENTER_VALID_VALUE
        self.assertRaisesRegexp(ValidationError, error_message, org.full_clean)

    def test_creating_duplicate_organization(self):
        # Create Organization
        create_organization_with_details('DummyOrg')

        # Check database for org creation
        self.assertEqual(len(Organization.objects.all()), 1)

        # Create duplicate Organization and check Error message
        error_message = 'duplicate key value violates unique constraint "organization_organization_name_key'
        error_statement = Organization.objects.create
        self.assertRaisesRegexp(IntegrityError, error_message, error_statement, name='DummyOrg')

    def test_organization_edit_with_valid_values(self):
        # Create Organization
        org = create_organization_with_details('DummyOrg')

        # Check database for org creation
        self.assertEqual(len(Organization.objects.all()), 1)

        org_in_db = Organization.objects.get(Q(name='DummyOrg'))

        org_in_db.name = 'DummyOrgNew'
        org_in_db.save()

        org_in_db = Organization.objects.get(Q(name='DummyOrgNew'))

        # Check if save was successful
        self.assertNotEqual(org_in_db.name, org.name)

    def test_organization_edit_with_invalid_values(self):
        # Create Organization
        create_organization_with_details('DummyOrg')

        # Check database for org creation
        self.assertEqual(len(Organization.objects.all()), 1)

        org_in_db = Organization.objects.get(Q(name='DummyOrg'))
        org_in_db.name = 'Dummy~Org'

        # Check Error message
        error_message = BasePage.ENTER_VALID_VALUE
        self.assertRaisesRegexp(ValidationError, error_message, org_in_db.full_clean)

    def test_organization_delete(self):
        # Create Organization
        create_organization_with_details('DummyOrg')

        # Check database for Organization create
        self.assertEqual(len(Organization.objects.all()), 1)

        # Delete org
        org_in_db = Organization.objects.get(Q(name='DummyOrg'))
        org_in_db.delete()

        # Check if deleted.
        self.assertEqual(len(Organization.objects.all()), 0)

    def test_create_multiple_organization_method(self):
        org_list = Organization.create_multiple_organizations(3)

        # Check number of orgs created
        self.assertEqual(len(Organization.objects.all()), 3)

        # Check their names
        self.assertEqual(org_list[0].name, 'org-1')
        self.assertEqual(org_list[1].name, 'org-2')
        self.assertEqual(org_list[2].name, 'org-3')

    def test_model_representation(self):
        # Create Organization
        org = create_organization_with_details('DummyOrg')

        # Check __str__
        self.assertEqual(org.name, str(org))
