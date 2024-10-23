# product/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 
            'category', 
            'subcategory', 
            'buying_price', 
            'selling_price', 
            'stock_quantity', 
            'barcode', 
            'description', 
            'unit', 
            'active', 
            'is_service'
        ]
