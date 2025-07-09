from rest_framework import serializers
from .models import CartItem
from products.models import Product

class CartSerializer(serializers.ModelSerializer):
    product_name=serializers.ReadOnlyField(source='product.name')
    product_price=serializers.ReadOnlyField(source='product.price')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())  # ✅ THIS LINE FIXES IT

    class Meta:
        model=CartItem
        fields='__all__'
