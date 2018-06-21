# standard library
import re
from urllib.request import urlretrieve
import os

import PyPDF2
from PyPDF2.utils import PdfReadError

# third party
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Django
from django.contrib.staticfiles.testing import LiveServerTestCase

# local Django
from pom.pages.authenticationPage import AuthenticationPage
from pom.pages.volunteerProfilePage import VolunteerProfilePage
from shift.utils import create_volunteer_with_details


class VolunteerProfile(LiveServerTestCase):
    """
    """

    @classmethod
    def setUpClass(cls):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("dom.file.createInChild", True)
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.profile_page = VolunteerProfilePage(cls.driver)
        cls.authentication_page = AuthenticationPage(cls.driver)
        cls.wait = WebDriverWait(cls.driver, 20)
        cls.download_from_internet()
        super(VolunteerProfile, cls).setUpClass()

    def setUp(self):
        vol = [
            'Goku', "Son", "Goku", "Kame House", "East District",
            "East District", "East District", "9999999999", "idonthave@gmail.com"
        ]
        self.volunteer_1 = create_volunteer_with_details(vol)
        self.volunteer_1.unlisted_organization = 'Detective'
        self.volunteer_1.save()
        self.login_correctly()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        os.remove(os.getcwd() + '/DummyResume.pdf')
        os.remove(os.getcwd() + '/DummyZip.zip')
        super(VolunteerProfile, cls).tearDownClass()

    def login_correctly(self):
        self.authentication_page.server_url = self.live_server_url
        self.authentication_page.login({
            'username': "Goku",
            'password': "volunteer"
        })

    def wait_for_profile_load(self, profile_name):
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h1[contains(text(), '" + profile_name + "')]")
            )
        )

    def wait_for_home_page(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h1[contains(text(), 'Volunteer Management System')]")
            )
        )

    @staticmethod
    def download_from_internet():
        urlretrieve('https://dl.dropboxusercontent.com/s/08wpfj4n9f9jdnk/DummyResume.pdf',
                    'DummyResume.pdf')
        urlretrieve('https://dl.dropboxusercontent.com/s/uydlhww0ekdy6j7/DummyZip.zip',
                    'DummyZip.zip')

    def test_details_tab(self):
        profile_page = self.profile_page
        profile_page.navigate_to_profile()
        self.wait_for_profile_load('Son Goku')
        page_source = self.driver.page_source

        found_email = re.search(self.volunteer_1.email, page_source)
        self.assertNotEqual(found_email, None)

        found_city = re.search(self.volunteer_1.city, page_source)
        self.assertNotEqual(found_city, None)

        found_state = re.search(self.volunteer_1.state, page_source)
        self.assertNotEqual(found_state, None)

        found_country = re.search(self.volunteer_1.country, page_source)
        self.assertNotEqual(found_country, None)

        found_org = re.search(self.volunteer_1.unlisted_organization, page_source)
        self.assertNotEqual(found_org, None)

    def test_edit_profile(self):
        profile_page = self.profile_page
        profile_page.navigate_to_profile()
        self.wait_for_profile_load('Son Goku')
        profile_page.edit_profile()

        new_details = [
            'Harvey', 'Specter', 'hspecter@ps.com', 'Empire State Building',
            'NYC', 'New York', 'USA', '9999999998', 'None', 'Lawyer'
        ]
        profile_page.fill_values(new_details)
        self.wait_for_profile_load('Harvey Specter')

        page_source = self.driver.page_source

        found_email = re.search(self.volunteer_1.email, page_source)
        self.assertEqual(found_email, None)

        found_city = re.search(self.volunteer_1.city, page_source)
        self.assertEqual(found_city, None)

        found_state = re.search(self.volunteer_1.state, page_source)
        self.assertEqual(found_state, None)

        found_country = re.search(self.volunteer_1.country, page_source)
        self.assertEqual(found_country, None)

        found_org = re.search(self.volunteer_1.unlisted_organization, page_source)
        self.assertEqual(found_org, None)

        found_email = re.search(new_details[2], page_source)
        self.assertNotEqual(found_email, None)

        found_city = re.search(new_details[4], page_source)
        self.assertNotEqual(found_city, None)

        found_state = re.search(new_details[5], page_source)
        self.assertNotEqual(found_state, None)

        found_country = re.search(new_details[6], page_source)
        self.assertNotEqual(found_country, None)

        found_org = re.search(new_details[9], page_source)
        self.assertNotEqual(found_org, None)

    def test_invalid_resume_format(self):
        self.wait_for_home_page()

        path = os.getcwd() + '/DummyZip.zip'
        profile_page = self.profile_page
        profile_page.navigate_to_profile()
        self.wait_for_profile_load('Son Goku')
        profile_page.edit_profile()
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//legend[contains(text(), 'Edit Profile')]")
            )
        )

        profile_page.upload_resume(path)
        profile_page.submit_form()
        self.assertEqual(profile_page.get_invalid_format_error(), 'Uploaded file is invalid.')

# Resume Upload is buggy, it is taking too long to be uploaded on travis.
# https://github.com/systers/vms/issues/776


'''
    def test_valid_upload_resume(self):
        self.wait_for_home_page()

        path = os.getcwd() + '/DummyResume.pdf'
        profile_page = self.profile_page
        profile_page.navigate_to_profile()
        self.wait_for_profile_load('Son Goku')
        profile_page.edit_profile()
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//legend[contains(text(), 'Edit Profile')]")
            )
        )
        self.assertEqual(os.path.exists(path), True)

        profile_page.upload_resume(path)
        profile_page.submit_form()
        self.wait_for_profile_load('Son Goku')
        self.assertEqual(profile_page.download_resume_text(), 'Download Resume')

    def test_corrupt_resume_uploaded(self):
        """
        Check if uploaded resume is corrupt.
        """
        self.wait_for_home_page()
        path = os.getcwd() + '/DummyResume.pdf'
        size_before_upload = os.stat(path).st_size
        profile_page = self.profile_page
        profile_page.navigate_to_profile()
        self.wait_for_profile_load('Son Goku')
        profile_page.edit_profile()
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//legend[contains(text(), 'Edit Profile')]")
            )
        )
        self.assertEqual(os.path.exists(path), True)

        profile_page.upload_resume(path)
        profile_page.submit_form()

        self.wait_for_profile_load('Son Goku')
        self.assertEqual(profile_page.download_resume_text(), 'Download Resume')
        path = os.getcwd() + '/srv/vms/resume/DummyResume.pdf'
        size_after_upload = os.stat(path).st_size

        # Check via size
        self.assertEqual(size_after_upload, size_before_upload)

        # Check via open
        try:
            PyPDF2.PdfFileReader(open(path, 'rb'))
        except PdfReadError:
            print('Some error while upload/download')
        else:
            pass
'''
