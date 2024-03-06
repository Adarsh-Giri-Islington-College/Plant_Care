from django.contrib import admin
from . models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_image','product_name', 'product_price', 'product_description', 'added_at')

admin.site.register(Product, ProductAdmin)
