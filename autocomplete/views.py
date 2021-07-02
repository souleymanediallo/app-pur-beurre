from django.shortcuts import render
from django.http import JsonResponse

from catalog.models import Product


# Create your views here.
def complete(request):
    searched_name_product = request.GET.get("query")
    products = Product.objects.filter(name__icontains=searched_name_product).order_by("-nutrition_grade")[:20]
    products = [product.name for product in products]
    return JsonResponse(products, safe=False)