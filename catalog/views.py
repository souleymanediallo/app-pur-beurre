from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Product, Favorite


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


@login_required
def add_favorite(request, product_id):
    try:
        Favorite.objects.get(user_name_id=request.user.id, product_id=(product_id))
        messages.warning(request, 'Ce produit est déjà dans vos favoris.')
        return redirect(request.META.get('HTTP_REFERER'))

    except ObjectDoesNotExist:
        Favorite.objects.create(user_name_id=request.user.id, product_id=(product_id))
        messages.success(request, 'Ce produit a été enregistré.')
        return redirect(request.META.get('HTTP_REFERER'))


@login_required
def my_favorite(request):
    favorites = Favorite.objects.all()
    context = {"favorites": favorites}
    return render(request, "catalog/product_favorites.html", context)


@login_required
def delete_favorite(request, product_id):
    favorit = get_object_or_404(Favorite, pk=product_id)
    if request.method == "POST":
        favorit.delete()
        messages.success(request, 'Ce produit a été supprimé')
        return redirect("catalog:my-favorite")
    return render(request, "catalog/delete_favorite.html")
