from django.test import SimpleTestCase
from django.urls import reverse


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('register')
        print(reverse(url))