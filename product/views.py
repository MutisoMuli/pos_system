from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category, SubCategory
from .forms import ProductForm, CategoryForm
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
import csv
import openpyxl  # Add this import for handling Excel files

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

def import_products(request):
    if request.method == 'POST':
        file = request.FILES['file']
        if file.name.endswith('.csv'):
            decoded_file = file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            for row in reader:
                # Assuming your CSV structure: name, category_id, subcategory_id, buying_price, selling_price, etc.
                Product.objects.create(
                    name=row[0],
                    category_id=row[1],
                    subcategory_id=row[2],
                    buying_price=row[3],
                    selling_price=row[4],
                    stock_quantity=row[5],
                    barcode=row[6],
                    description=row[7],
                    unit=row[8],
                    active=row[9] == 'True',
                    is_service=row[10] == 'True'
                )
            messages.success(request, 'Products imported successfully!')
        elif file.name.endswith('.xlsx'):
            wb = openpyxl.load_workbook(file)
            sheet = wb.active
            for row in sheet.iter_rows(min_row=2, values_only=True):
                Product.objects.create(
                    name=row[0],
                    category_id=row[1],
                    subcategory_id=row[2],
                    buying_price=row[3],
                    selling_price=row[4],
                    stock_quantity=row[5],
                    barcode=row[6],
                    description=row[7],
                    unit=row[8],
                    active=row[9] == 'True',
                    is_service=row[10] == 'True'
                )
            messages.success(request, 'Products imported successfully!')
        return redirect('product-list')

    return render(request, 'import_products.html')

def export_products(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Category', 'SubCategory', 'Buying Price', 'Selling Price', 'Stock Quantity', 'Barcode', 'Description', 'Unit', 'Active', 'Is Service'])
    for product in Product.objects.all():
        writer.writerow([
            product.name,
            product.category.name if product.category else '',
            product.subcategory.name if product.subcategory else '',
            product.buying_price,
            product.selling_price,
            product.stock_quantity,
            product.barcode,
            product.description,
            product.unit,
            product.active,
            product.is_service
        ])
    return response
