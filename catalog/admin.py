from django.contrib import admin
from .models import Category, Product, Favorite


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "brand"]
    list_display_links = ["name"]


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ["user_name"]
    list_display_links = ["user_name"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Favorite, FavoriteAdmin)