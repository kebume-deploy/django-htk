"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

####################
# Finally, import tests from subdirectories last to prevent circular import
from htk.lib.geoip.tests import *
from htk.lib.google.tests import *
from htk.lib.qrcode.tests import *
from htk.lib.stripe_lib.tests import *
