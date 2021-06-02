from django.test import TestCase
import unittest

from catalog.models import Category


# class CategoryModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         Category.objects.create(name='Pizza')
#
#     def test_first_name_label(self):
#         category = Category.objects.get(id=1)
#         field_label = category._meta.get_field('name').verbose_name
#         self.assertEquals(field_label, 'name')
#
#     def test_first_name_max_length(self):
#         category = Category.objects.get(id=1)
#         max_length = category._meta.get_field('name').max_length
#         self.assertEquals(max_length, 200)
#
#
# if __name__ == '__main__':
#     unittest.main()

