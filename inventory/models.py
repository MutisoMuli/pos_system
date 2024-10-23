from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from products.models import Product

class StockAdjustment(models.Model):
    ADJUSTMENT_TYPES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
        ('ADJ', 'Adjustment')
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    adjustment_type = models.CharField(max_length=3, choices=ADJUSTMENT_TYPES)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    reference_number = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if self.adjustment_type == 'IN':
            self.product.stock_quantity += self.quantity
        elif self.adjustment_type == 'OUT':
            if self.product.stock_quantity >= self.quantity:
                self.product.stock_quantity -= self.quantity
            else:
                raise ValidationError("Insufficient stock quantity")
        else:  # ADJ
            self.product.stock_quantity = self.quantity
        
        self.product.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_adjustment_type_display()} - {self.product.name}"
