import unittest
from django.test import TestCase


class UnitTestCase(TestCase):

    def test_homepage_template(self):
        response = self.client.get('frontend:home')
        self.assertTemplateUsed(response, "frontend/index.html")


if __name__ == '__main__':
    unittest.main()

