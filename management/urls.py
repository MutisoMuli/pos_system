# management/urls.py
from django.urls import path, include
from .views import management_home

urlpatterns = [
    path('', management_home, name='management'),
    path('product/', include('product.urls')),      # Include product app URLs
    path('dashboard/', include('dashboard.urls')),  # Include dashboard app URLs
]
