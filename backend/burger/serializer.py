from rest_framework import serializers
from .models import Customer, Product, CxP

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id','servicio', 'pago')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id','name', 'imagen', 'tipo', 'precio')


class CxPSerializer(serializers.ModelSerializer):
    Product = ProductSerializer(many=True)
    Customer = CustomerSerializer(many=True)

    class Meta:
        model = CxP
        fields = ('unidad')