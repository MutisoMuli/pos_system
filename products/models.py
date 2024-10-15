from django.db import models
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    VARIANT_CHOICES = [
        ('none', 'None'),
        ('size', 'Size'),
        ('color', 'Color'),
        ('size_color', 'Size & Color'),
    ]

    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, unique=True)
    barcode = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock_quantity = models.IntegerField(default=0)
    minimum_stock = models.IntegerField(default=10)
    variant_type = models.CharField(max_length=20, choices=VARIANT_CHOICES, default='none')
    image = models.ImageField(upload_to='products/', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    default_quantity = models.BooleanField(default=False)
    is_service = models.BooleanField(default=False)
    unit = models.CharField(max_length=50, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.buying_price and self.price:
            self.buying_price = self.price
        if not self.selling_price and self.price:
            self.selling_price = self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

    @property
    def low_stock(self):
        return self.stock_quantity <= self.minimum_stock