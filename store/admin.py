"""
Admin configurations for the Product model, including custom admin classes 
and settings for the admin interface.
"""
from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    """Customizes the admin interface for the Product 
    model, including displayed fields and prepopulated slug."""
    list_display        = (
        'product_name',
        'price', 'stock',
        'category',
        'modified_date',
        'is_available'
        )
    prepopulated_fields = {'slug': ('product_name',)}

class VariationAdmin(admin.ModelAdmin):
    """
    Admin interface for managing product variations.
    Displays product, variation category, variation value, 
    and active status in the admin list view.
    """
    list_display    = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable   = ('is_active',)
    list_filter     = ('product', 'variation_category', 'variation_value')

admin.site.register(Product, ProductAdmin)

