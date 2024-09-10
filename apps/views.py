from random import randint

from django.core.cache import cache
from django.core.mail import send_mail
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from root import settings
from .filter import UnitFilterSet
from .models import User, Books, Units, AdminSiteSettings, Test
from .serializer import UserModelSerializer, BooksModelSerializer, UnitsModelSerializer, \
    AdminSiteSettingsModelSerializer, TestModelSerializer, VerifyModelSerializer, EmailModelSerializer


@extend_schema(tags=['user'])
class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


@extend_schema(tags=['book'])
class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksModelSerializer


@extend_schema(tags=['units'])
class UnitsViewSet(ModelViewSet):
    queryset = Units.objects.all()
    serializer_class = UnitsModelSerializer
    filterset_class = UnitFilterSet


@extend_schema(tags=['admin_settings'])
class AdminSiteSettingsListCreateAPIView(ListCreateAPIView):
    queryset = AdminSiteSettings.objects.all()
    serializer_class = AdminSiteSettingsModelSerializer


@extend_schema(tags=['test'])
class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestModelSerializer


@extend_schema(tags=['send-email'])
class SendEmailAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = EmailModelSerializer
    permission_classes = AllowAny,

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        code = randint(100000, 10000000)
        cache.set(email, code, timeout=120)
        send_mail(subject="HI", message=f"Hello My Friend Your Verify Code {code}", from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[email])
        print(f'Email:{email}, Code:{code}')
        return Response({"message": "Successfully sent code"})

    def get_queryset(self):
        return self.request.user


@extend_schema(tags=['send-email'])
class VerifyEmailAPIView(GenericAPIView):
    serializer_class = VerifyModelSerializer
    permission_classes = IsAuthenticated,

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "OK"})
