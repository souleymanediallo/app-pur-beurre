from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path('search', views.search, name="search"),
    path('products', views.product_list, name="products"),
    path('products/<int:product_id>', views.product_detail, name="detail"),
]