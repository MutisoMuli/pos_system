# product/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    barcode = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    unit = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    is_service = models.BooleanField(default=False)
