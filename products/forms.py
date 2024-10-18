from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    new_category = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text="Enter a new category if not in the list"
    )

    class Meta:
        model = Product
        fields = [
            'name', 'sku', 'category', 'description',
            'buying_price', 'selling_price', 'active', 
            'is_service', 'unit'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'buying_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_service': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].empty_label = "Select a category"

    def clean_category(self):
        category = self.cleaned_data.get('category')
        new_category = self.cleaned_data.get('new_category')

        if not category and not new_category:
            raise forms.ValidationError("Please select an existing category or enter a new one.")
        
        if new_category:
            category, created = Category.objects.get_or_create(name=new_category)
            return category
        
        return category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 3})
