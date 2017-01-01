from django.core.cache import cache
from django.test import TestCase
from authentication.views import login_process
from django.contrib.auth.models import User
from django.test.client import RequestFactory


# Create your tests here.
class TestLoginProcess(TestCase):

	def testLoginViewRateLimit(self):
		request = RequestFactory().post("/login")
		request.user = User.objects.create_user(
			username='Test User', email='test@a.com', password='Password')
		for loginAttemp in range(25):
			response = login_process(request)
			# redirection on sucessfull authentication
			self.assertEqual(login_process(request).status_code, 302)
		# 26th attempt should error
		self.assertEqual(login_process(request).status_code, 429)

	def tearDown(self):
		#from IPython import embed; embed();
		cache.clear()
		User.objects.all().delete()
