from random import randint

from django.core.cache import cache
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.filters import UnitFilterSet, TestFilterSet
from apps.models import User, Books, Units, AdminSiteSettings, Test
from apps.serializer import UserModelSerializer, BooksModelSerializer, UnitsModelSerializer, \
    AdminSiteSettingsModelSerializer, TestModelSerializer, VerifyModelSerializer, EmailModelSerializer, \
    SendEmailSerializer, VerificationCodeSerializer
from apps.tasks import send_verification_email1, send_verification_email_task


@extend_schema(tags=['user'])
class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


# def post(self, request, *args, **kwargs):
#     password = request.POST['password']
#     email = request.POST['email']


# def create(self, request, *args, **kwargs):
#     password = request.data['password']
#     request.data['password'] = make_password(password)
#     return super().create(request, *args, **kwargs)


@extend_schema(tags=['send-email2'])
class SendEmail(APIView):
    permission_classes = [AllowAny]
    serializer_class = SendEmailSerializer

    def post(self, request):
        serializer = SendEmailSerializer(data=request.data)
        if serializer.is_valid():
            receiver_email = serializer.validated_data['email']
            send_verification_email1.delay(receiver_email)
            return Response({"message": "Check Email"}, status=200)
        return Response(serializer.errors, status=400)


@extend_schema(tags=['send-email2'])
class VerificationCode(APIView):
    serializer_class = VerificationCodeSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = VerificationCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "OK"})



@extend_schema(tags=['book'])
class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksModelSerializer
    permission_classes = [AllowAny, ]




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
    filterset_class = TestFilterSet


@extend_schema(tags=['send-email'])
class SendEmailAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = EmailModelSerializer
    permission_classes = AllowAny,

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        code = randint(100000, 1000000)
        cache.set(email, code, timeout=120)
        send_verification_email_task.delay(email, code)
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
