from django.test import TestCase
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait


# class FunctionalTestCase(TestCase):
#
#     def setUp(self):
#         self.browser = Chrome()
#
#     def test_there_is_homepage(self):
#         self.browser.get('https://app-pur-beurre.herokuapp.com/')
#         WebDriverWait(self.browser, 20)
#         self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         research_input = self.browser.find_element_by_name("query")
#         research_input.send_keys("Pizza")
#         WebDriverWait(self.browser, 20)
#         self.browser.find_element_by_class_name("btn").click()
#
#     def tearDown(self):
#         self.browser.implicitly_wait(60)
#         self.browser.quit()
