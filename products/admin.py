from django.contrib import admin
from .models import Product, offer

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class offerAdmin(admin.ModelAdmin): 
    list_display = ('code', 'discount')


admin.site.register(Product, ProductAdmin)
admin.site.register(offer, offerAdmin)