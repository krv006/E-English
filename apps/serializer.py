from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.fields import EmailField, CharField
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Units, Books, User, AdminSiteSettings, Test


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'email', 'password'


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
