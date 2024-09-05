from rest_framework.serializers import ModelSerializer

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
