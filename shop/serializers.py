from jazzmin.templatetags.jazzmin import User

from shop.models import Category, Product, Picture, Order, OrderItem, Address
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PictureSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Picture
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    stock_price = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_images(self, obj):
        return [image.image.url for image in obj.images.all()]

    def get_stock_price(self, obj):
        return obj.price * (100 - obj.stock) / 100

    def get_total_price(self, obj):
        return self.get_stock_price(obj) * obj.quantity

    def get_price(self, obj):
        return float(obj.price)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {k: representation[k] for k in sorted(representation)}


class UserSerializer:
    class Meta:
        model = User
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()
    user = UserSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
