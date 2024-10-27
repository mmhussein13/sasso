"""
This module defines the `Product` model, which represents products in the system,
including details such as name, description, price, images, stock availability, and 
association with categories.
"""
from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.
class Product(models.Model):
    """
    Represents a product in the system with details such as name, description, 
    pricing, stock, images, and availability. Each product is associated with 
    a category and tracks its creation and modification dates.
    """
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    images           = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return str(self.product_name)
