from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Product


# Create your views here.
def search(request):
    query = request.GET.get('query')
    try:
        product = Product.objects.filter(name=query).first()
        substitutes = Product.objects.filter(category=product.category).order_by("nutrition_grade")[:12]
        products = substitutes
        context = {
            'products': products,
            'paginate': True,
            'title': query,
            'image': product.picture,
        }
    except AttributeError:
        messages.warning(request, "Ce produit n'est pas disponible, essayer un autre produit")
        return redirect('frontend:home')

    return render(request, 'catalog/search.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
        'title': product.name,
        'image': product.picture,
    }
    return render(request, 'catalog/product_detail.html', context)


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/product_list.html', context)