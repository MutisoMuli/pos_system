from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('category/<int:category_id>/', views.product_list, name='category-products'),
    path('product/create/', views.product_create, name='product-create'),
    path('product/delete/<int:product_id>/', views.product_delete, name='product-delete'),
    path('category/delete/<int:category_id>/', views.category_delete, name='category-delete'),
    path('category/edit/<int:category_id>/', views.category_edit, name='category-edit'),
]
