from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, CASCADE, TextField, ForeignKey, SlugField, CharField, DateTimeField
from django.db.models import Model, FloatField
from django.utils.text import slugify


class BaseSlugModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1
            while self.__class__.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(BaseSlugModel):
    pass


class Product(BaseSlugModel):
    price = FloatField(default=0)
    discount = FloatField(default=0)
    description = TextField(null=True, blank=True)
    category = ForeignKey('apps.Category', CASCADE, related_name='product_category')
