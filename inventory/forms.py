from django import forms
from .models import StockAdjustment

class StockAdjustmentForm(forms.ModelForm):
    class Meta:
        model = StockAdjustment
        fields = ['product', 'adjustment_type', 'quantity', 'unit_price', 'reference_number', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        quantity = cleaned_data.get('quantity')
        adjustment_type = cleaned_data.get('adjustment_type')
        
        if product and quantity and adjustment_type:
            if adjustment_type == 'OUT' and product.stock_quantity < quantity:
                raise forms.ValidationError(
                    f"Insufficient stock. Available: {product.stock_quantity} {product.unit}"
                )
        return cleaned_data