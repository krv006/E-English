from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.fields import EmailField, CharField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import Order, Address, CategoryOfEggs, Employees, Customers, CustomerStatistics


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class AddressModelSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CategoryOfEggsModelSerializer(ModelSerializer):
    class Meta:
        model = CategoryOfEggs
        fields = '__all__'


class EmployeesModelSerializer(ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'


class CustomersModelSerializer(ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class CustomerStatisticsModelSerializer(ModelSerializer):
    class Meta:
        model = CustomerStatistics
        fields = '__all__'


class EmailModelSerializer(Serializer):
    email = EmailField(help_text='Enter email')


class VerifyModelSerializer(Serializer):
    email = EmailField(help_text='Enter email')
    code = CharField(max_length=8, help_text='Enter confirmation code')

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')
        cache_code = str(cache.get(email))
        if code != cache_code:
            raise ValidationError('Code not found or timed out')

        return attrs
