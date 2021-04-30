from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="product"
    )
    brand = models.CharField(max_length=200)
    nutrition_grade = models.CharField(max_length=1)
    picture = models.URLField()
    nutrition_image = models.URLField()
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name", "nutrition_grade"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:detail", kwargs={"product_id": self.pk})


class Favorite(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.user_name} "

    def get_absolute_url(self):
        return reverse("catalog:delete-favorite", kwargs={"product_id": self.pk})
