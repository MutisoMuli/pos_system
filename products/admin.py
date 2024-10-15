from django.contrib import admin
from .models import Product, Category, ProductCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'buying_price', 'selling_price', 'stock_quantity', 'active')
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
            'fields': ('stock_quantity', 'minimum_stock', 'unit')
        }),
        ('Options', {
            'fields': ('variant_type', 'active', 'default_quantity', 'is_service')
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