from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('create/', views.product_create, name='product-create'),
]