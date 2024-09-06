from random import randint

from django.core.cache import cache
from django.core.mail import send_mail
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from apps.models import Order, Address, CategoryOfEggs, Employees, Customers, CustomerStatistics
from apps.serializer import OrderModelSerializer, AddressModelSerializer, CategoryOfEggsModelSerializer, \
    EmployeesModelSerializer, CustomersModelSerializer, CustomerStatisticsModelSerializer, VerifyModelSerializer, \
    EmailModelSerializer
from root import settings


@extend_schema(tags=['order'])
class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


@extend_schema(tags=['order_detail'])
class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


@extend_schema(tags=['address_detail'])
class AddressRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressModelSerializer


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


@extend_schema(tags=['employees_detail'])
class EmployeesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesModelSerializer


@extend_schema(tags=['customers'])
class CustomersListCreateAPIView(ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersModelSerializer


@extend_schema(tags=['customers-statistic'])
class CustomerStatisticsListCreateAPIView(ListCreateAPIView):
    queryset = CustomerStatistics.objects.all()
    serializer_class = CustomerStatisticsModelSerializer

# todo ModelViewSet mana shunda xammasi bor va shunda xammasi ishlidi`
# todo login email orqali login qilish


class SendEmailAPIView(GenericAPIView):
    serializer_class = EmailModelSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        code = randint(100000, 10000000)
        cache.set(email, code, timeout=120)
        print(code)
        send_mail(subject="HI", message=f"Hello My Friend Your Verify Code {code}", from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[email])
        print(f'Email:{email}, Code:{code}')
        return Response({"message": "Successfully sent code"})

    def get_queryset(self):
        return self.request.user


class VerifyEmailAPIView(GenericAPIView):
    serializer_class = VerifyModelSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "OK"})