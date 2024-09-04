from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from apps.models import Category, Product
from apps.serializer import CategoryModelSerializer, ProductModelSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
