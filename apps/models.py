from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CASCADE, ForeignKey, CharField, DateTimeField, \
    BigIntegerField, IntegerField
from django.db.models import Model, FloatField


class CategoryOfEggs(Model):
    name = CharField(max_length=255)
    price = BigIntegerField(default=0)

    def __str__(self):
        return self.name


class Order(Model):
    customer = ForeignKey('apps.Customers', on_delete=CASCADE, related_name='orders')
    egg_count = IntegerField(default=0)
    egg = ForeignKey('apps.CategoryOfEggs', on_delete=CASCADE, related_name='orders')
    total = FloatField(default=0)
    order_date = DateTimeField(auto_now_add=True)
    status = CharField(max_length=255)

    def __str__(self):
        return f"Order {self.id} - {self.status}"


class CustomerStatistics(Model):
    customer = ForeignKey('apps.Customers', on_delete=CASCADE, related_name='statistics')
    residual = FloatField(default=0)
    order = ForeignKey('apps.Order', on_delete=CASCADE, related_name='statistics')
    telegram_link = CharField(max_length=255)

    def __str__(self):
        return f"Stats for Customer {self.customer_id}"


class Customers(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    phone_number = CharField(max_length=255)
    address = ForeignKey('apps.Address', on_delete=CASCADE, related_name='residents')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Payment(Model):
    customer = ForeignKey('apps.Customers', on_delete=CASCADE, related_name='payments')
    dealer_id = BigIntegerField(default=0)
    amount = IntegerField(default=0)
    payment_date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} by {self.customer}"


class Address(Model):
    region = CharField(max_length=255)
    district = CharField(max_length=255)
    target = CharField(max_length=255)

    def __str__(self):
        return f"{self.region}, {self.district}, {self.target}"


class Employees(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    role_name = CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role_name}"
