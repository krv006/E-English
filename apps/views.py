from random import randint

from django.core.cache import cache
from django.core.mail import send_mail
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response



# @extend_schema(tags=['order'])
# class OrderListCreateAPIView(ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderModelSerializer


