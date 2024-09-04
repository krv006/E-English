from django.db import models
from django.db.models import Model, CharField, ForeignKey, CASCADE, IntegerField, TextField, DateTimeField


class Category(Model):
    name = CharField(max_length=255)


class Product(Model):
    name = CharField(max_length=255)
    price = IntegerField(default=0)
    description = TextField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    category = ForeignKey('apps.Category', CASCADE, related_name='product_category')
