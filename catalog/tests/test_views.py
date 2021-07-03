from django.test import Client, TestCase
from django.urls import reverse
from catalog.models import Product, Category
from accounts.models import CustomUser


class TestProductView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username="hello",
            email="hello@gmail.com",
            password="Paris1234",
        )
        self.client.login(
            email="hello@gmail.com",
            password="Paris1234",
        )

    def test_create_category(self):
        nbr_of_category_before_add = Category.objects.count()

        new_category = Category()
        new_category.name = "Moins de gras"
        new_category.save()

        nbr_of_category_after_add = Category.objects.count()

        self.assertTrue(nbr_of_category_after_add == nbr_of_category_before_add + 1)


class CategoryProduct(TestCase):
    def setUp(self):
        new_category = Category()
        new_category.name = "Moins de gras"
        new_category.save()


class TestProductDetailView(TestCase):
    def setUp(self):
        self.category = category = Category.objects.create(name="NewCate")
        self.product = Product.objects.create(
            name="Pomme",
            category=category,
            brand="Dominos",
            nutrition_grade="e",
            picture="https://images.pexels.com/photos/1260968/pexels-photo-1260968.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
            nutrition_image="https://images.pexels.com/photos/1260968/pexels-photo-1260968.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
            url="https://www.pexels.com/fr-fr/chercher/pizza/",
        )
        self.product.save()

    def test_url_product_detail(self):
        url = reverse("catalog:detail", kwargs={'product_id': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

