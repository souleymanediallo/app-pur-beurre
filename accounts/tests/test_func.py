from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

from selenium.webdriver import Chrome


# https://www.selenium.dev/documentation/fr/webdriver/understanding_the_components/
class ProductResearchTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_research_product_with_home_buttom(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/"))
        research_input = self.selenium.find_element_by_id("search")
        research_input.send_keys("Nutella")
        self.selenium.find_element_by_class_name("btn").click()

# class FunctionalTestCase(TestCase):
#
#     def setUp(self):
#         self.browser = Chrome()
#
#     def test_there_is_homepage(self):
#         self.browser.get('http://localhost:8000/')
#         self.assertIn('Afficher', self.browser.page_source)
#
#     def tearDown(self):
#         self.browser.quit()

