from django.contrib import admin
from .models import Product, Category, ProductCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Updated list_display to match Product model fields
    list_display = (
        'name', 
        'sku', 
        'category', 
        'buying_price', 
        'selling_price', 
        'active'
    )  # Removed 'stock_quantity'

    list_filter = ('category', 'active', 'is_service')
    search_fields = ('name', 'sku', 'description')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        (None, {
            'fields': ('name', 'sku', 'barcode', 'category', 'description')
        }),
        ('Pricing', {
            'fields': ('buying_price', 'selling_price')
        }),
        ('Stock', {
            'fields': ('minimum_stock', 'unit')  # Removed 'stock_quantity'
        }),
        ('Options', {
            'fields': ('variant_type', 'active', 'is_service')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
