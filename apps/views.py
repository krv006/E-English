from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from drf_spectacular.utils import extend_schema

from apps.models import Order, Address, CategoryOfEggs, Employees, Customers, CustomerStatistics
from apps.serializer import OrderModelSerializer, AddressModelSerializer, CategoryOfEggsModelSerializer, \
    EmployeesModelSerializer, CustomersModelSerializer, CustomerStatisticsModelSerializer


@extend_schema(tags=['order'])
class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


@extend_schema(tags=['order_detail'])
class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer

@extend_schema(tags=['address'])
class AddressListCreateAPIView(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressModelSerializer


@extend_schema(tags=['category_of_eggs'])
class CategoryOfEggsListCreateAPIView(ListCreateAPIView):
    queryset = CategoryOfEggs.objects.all()
    serializer_class = CategoryOfEggsModelSerializer


@extend_schema(tags=['employees'])
class EmployeesListCreateAPIView(ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesModelSerializer


@extend_schema(tags=['customers'])
class CustomersListCreateAPIView(ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersModelSerializer


@extend_schema(tags=['customers'])
class CustomerStatisticsListCreateAPIView(ListCreateAPIView):
    queryset = CustomerStatistics.objects.all()
    serializer_class = CustomerStatisticsModelSerializer
