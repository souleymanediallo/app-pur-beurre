from django.test import TestCase

from catalog.models import Category


class CategoryTestCase(TestCase):
    def test_create_category(self):
        nbr_of_category_before_add = Category.objects.count()

        new_category = Category()
        new_category.name = "Moins de gras"
        new_category.save()

        nbr_of_category_after_add = Category.objects.count()

        self.assertTrue(nbr_of_category_after_add == nbr_of_category_before_add + 1)
