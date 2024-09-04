from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product
from rest_framework.fields import IntegerField


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    price = IntegerField(default=0)

    class Meta:
        model = Product
        fields = '__all__'
        # exclude = 'id',

    def to_representation(self, instance: Product):
        repr = super().to_representation(instance)
        repr['category'] = CategoryModelSerializer(instance.category).data
        # repr['key'] = 'value' #todo buyodan xolagan narsamizani qoshib qoyse boladi
        return repr
