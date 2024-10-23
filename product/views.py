from django.shortcuts import render, redirect
from .models import Product, Category, SubCategory  # Now you can import SubCategory
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()  # Get all products
    return render(request, 'product_list.html', {'products': products})

from .models import Product, Category, SubCategory
from .forms import ProductForm



from django.contrib import messages

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

def product_list(request):
    return render(request, 'product_list.html', {
        'products': Product.objects.all(),
        'categories': Category.objects.all(),
    })
