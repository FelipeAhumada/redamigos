"""
Tests for the user app
"""
# standard
import json

# django
from django.core.urlresolvers import reverse
from redamigos.apps.user.models import User

# tests
from django.test import TestCase


class UserTests(TestCase):
    def test_lower_case_emails(self):
        """
        Tests that users are created with lower case emails
        """
        self.user.email = "Hello@magnet.cl"
        self.user.save()
        self.assertEqual(self.user.email, 'hello@magnet.cl')

    def test_force_logout(self):
        """
        Tests that users are created with lower case emails
        """
        url = reverse('password_change')
        response = self.client.get(url)

        # test that the user is logged in
        self.assertEqual(response.status_code, 200)

        self.user.force_logout()

        response = self.client.get(url)

        # user is logged out, sow redirects to login
        self.assertEqual(response.status_code, 302)
