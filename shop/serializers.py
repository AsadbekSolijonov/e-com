from shop.models import Category, Product, Picture, Order, OrderItem, Address
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

