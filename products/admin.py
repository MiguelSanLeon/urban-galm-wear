from django.contrib import admin
from .models import Product, Category
from django import forms


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['user_wishlist']


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = (
        'sku',
        'name',
        'category',
        'rating',
        'carbon_footprint',
        'price',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
