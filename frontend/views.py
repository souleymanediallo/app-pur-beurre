from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "frontend/index.html")


def mentions_legales(request):
    return render(request, "frontend/mentions-legales.html")