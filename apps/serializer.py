from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.fields import EmailField, CharField
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Units, Books, User, AdminSiteSettings, Test


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')  # Eslatma: bu yerda qavslar kiritildi

        # Tavsiya qilinmaydi, lekin agar vaqtincha kerak bo'lsa:
        # todo bunda write_only bolganda yoziladi lekin post va get qilganda korinmaydi swaggerda
        # extra_kwargs = {
        #     "password": {
        #         "write_only": True,
        #     }
        # }

        # todo bunda read_only bolgani uchun faqat korsa boladi va ozgartirish kiritib bolmaydi
        # extra_kwargs = {
        #     "password": {
        #         "read_only": True,
        #     }
        # }

    def validate(self, attrs):
        password = attrs.get('password')
        if password:
            attrs['password'] = make_password(password)  # 'password' string sifatida ishlatiladi
        return super().validate(attrs)


class VerificationCodeSerializer(Serializer):
    email = EmailField()
    code = CharField(max_length=6, help_text='Enter confirmation code')

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')
        cache_code = str(cache.get(email))
        if code != cache_code:
            raise ValidationError('Code not found or timed out')
        return attrs


class BooksModelSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class UnitsModelSerializer(ModelSerializer):
    class Meta:
        model = Units
        fields = '__all__'

    def to_representation(self, instance: Units):
        repr = super().to_representation(instance)
        repr['book'] = BooksModelSerializer(instance.book, context=self.context).data
        return repr


class AdminSiteSettingsModelSerializer(ModelSerializer):
    class Meta:
        model = AdminSiteSettings
        fields = '__all__'


class TestModelSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

    def to_representation(self, instance: Test):
        repr = super().to_representation(instance)
        repr['unit'] = UnitsModelSerializer(instance.unit, context=self.context).data
        return repr


class SendEmailSerializer(Serializer):
    email = EmailField()


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
