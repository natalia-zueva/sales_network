from rest_framework import serializers

from network.models import NetworkUnit, Product


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = NetworkUnit
        fields = '__all__'


class UnitUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = NetworkUnit
        exclude = ['debt']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
