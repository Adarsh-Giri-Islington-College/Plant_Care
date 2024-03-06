from django.db import models
from datetime import datetime
from django import forms


class Product(models.Model):
    product_image = models.ImageField(null=False, blank=False)
    product_name = models.CharField(max_length=200, null=False, blank=False)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField()  
    added_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.product_name
    

class product_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_image', 'product_name', 'product_price', 'product_description')
        widgets = {
            'product_image': forms.FileInput(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_price': forms.TextInput(attrs={'class': 'form-control'}),
            'product_description': forms.TextInput(attrs={'class': 'form-control'}),
        }

