"""pydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/

"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

def trigger_error(request):
    division_by_zero = 1 / 0
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('account/', include('accounts.urls')),
    path('catalog/', include('catalog.urls')),
    path('sentry-debug/', trigger_error),
    path('contact/', include('contact.urls')),
    path('autocomplete/', include('autocomplete.urls', namespace="autocomplete")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
