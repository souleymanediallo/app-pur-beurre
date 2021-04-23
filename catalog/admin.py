from django.contrib import admin
from .models import Category, Product, Favorite


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_filter = ["name"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "nutrition_grade", "brand"]
    list_display_links = ["name"]
    search_fields = ["name"]
    list_filter = ["nutrition_grade"]
    list_per_page = 50


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ["user_name"]
    list_display_links = ["user_name"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Favorite, FavoriteAdmin)