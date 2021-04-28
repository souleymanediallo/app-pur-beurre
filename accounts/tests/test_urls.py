from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import register


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('accounts:register')
        print(reverse(url))