from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import F
from .models import Product, Category, ProductCategory
from .forms import ProductForm, CategoryForm

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    ordering = ['-created_at']
    
    def get_queryset(self):
        return Product.objects.all() 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['low_stock_products'] = Product.objects.filter(
        #    stock_quantity__lte=F('minimum_stock'))
        return context

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/product_list.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product-list')
    template_name = 'products/product_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        new_category_name = self.request.POST.get('new_category')

        if new_category_name:
            category, created = Category.objects.get_or_create(name=new_category_name)
            form.instance.category = category

        form.instance.active = self.request.POST.get('active') == 'on'
        form.instance.default_quantity = self.request.POST.get('default_quantity') == 'on'
        form.instance.is_service = self.request.POST.get('is_service') == 'on'

        messages.success(self.request, 'Product created successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        messages.success(self.request, 'Product updated successfully!')
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Product deleted successfully!')
        return super().delete(request, *args, **kwargs)