from rest_framework import serializers
from products.models import Product
from cart.models import CartItem
from .models import Order,OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_name=serializers.ReadOnlyField(source='product.name')

    class Meta:
        model=OrderItem
        fields='__all__'
class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True,read_only=True)

    class Meta:
        model=Order
        fields='__all__'
