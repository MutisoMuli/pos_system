from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, SubCategory
from .forms import ProductForm, CategoryForm
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

def product_list(request, category_id=None):
    categories = Category.objects.all()
    
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': category_id
    })

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('product-list')
    else:
        form = ProductForm()
    
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('product-list')

def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        messages.success(request, f'Category "{category.name}" deleted successfully!')
        return redirect('product-list')

    return render(request, 'category_confirm_delete.html', {'category': category})

def category_edit(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category was updated successfully!')
            return redirect('category-products', category_id=category_id)
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'category_edit.html', {
        'form': form,
        'object': category
    })