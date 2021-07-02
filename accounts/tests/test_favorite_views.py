from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import CustomUser


class TestFavoriteView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username="testadmin",
            email="test@gmail.com",
            password="Paris2024"
        )
        self.client.login(
            email="test@gmail.com",
            password="Paris2024"
        )

    def test_display_favorite_page(self):
        response = self.client.get(reverse("catalog:favorite"))
        self.assertTemplateUsed(response, "catalog/product_favorites.html")
        self.assertEqual(response.status_code, 200)
