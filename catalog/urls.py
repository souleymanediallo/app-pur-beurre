from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path('search', views.search, name="search"),
    path('products', views.product_list, name="products"),
    path('products/<int:product_id>', views.product_detail, name="detail"),
    path('add_favorite/<str:product_id>/', views.add_favorite, name='favorite'),
    path('my-favorite', views.my_favorite, name="my-favorite"),
    path('delete-favorite/<int:product_id>', views.delete_favorite, name="delete-favorite"),
]