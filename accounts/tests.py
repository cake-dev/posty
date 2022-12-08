from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.

# accounts tests
class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        # this page requires a log in, so it should redirect to the login page
        self.assertEqual(response.status_code, 302)

    def test_homepage_view(self):
        response = self.client.get(reverse("posty:dashboard"))
        self.assertEqual(response.status_code, 302)
