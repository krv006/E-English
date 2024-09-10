from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from .models import User, Books, Units, AdminSiteSettings, Test


# from apps.models import Product
#
#
# class ProductFilterSet(FilterSet):
#     class Meta:
#         model = Product
#         fields = 'category',  # todo category ga tegishli productlarni chiqazib beradi


class UnitFilterSet(FilterSet):
    name = CharFilter(field_name='book__name', lookup_expr='icontains')

    class Meta:
        model = Units
        fields = 'book',


class TestFilterSet(FilterSet):
    name = CharFilter(field_name='unit__name', lookup_expr='icontains')

    class Meta:
        model = Test
        fields = 'unit',
