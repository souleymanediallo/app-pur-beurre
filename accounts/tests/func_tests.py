from django.test import TestCase
from selenium.webdriver import Chrome


# https://www.selenium.dev/documentation/fr/webdriver/understanding_the_components/
class FunctionalTestCase(TestCase):

    def setUp(self):
        self.browser = Chrome()

    def test_there_is_homepage(self):
        self.browser.get('http://localhost:8000/')
        self.assertIn('Afficher', self.browser.page_source)

    def tearDown(self):
        self.browser.quit()