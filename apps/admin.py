from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Category, Product


# Register your models here.

@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    pass
