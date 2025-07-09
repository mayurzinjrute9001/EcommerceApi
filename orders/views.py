from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order,OrderItem
from .serializers import OrderItemSerializer,OrderSerializer
from cart.models import CartItem
from products.models import Product
# Create your views here.

class PlaceOrderView(APIView):
    def post(self,request):
        cart_items=CartItem.objects.filter(user=request.user)
        if not cart_items.exists():
            return Response({'error':'cart is empty'},status=400)
        shipping_address=request.data.get('shipping_address')
        if not shipping_address:
            return Response({'error':'address is required'},status=400)

        total = sum(item.product.price * item.quantity for item in cart_items)
        order=Order.objects.create(user=request.user,shipping_address=shipping_address,total_price=total)

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )
            item.delete()
        serializer=OrderSerializer(order)
        return Response(serializer.data,status=201)

class UserOrderListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        serializer=OrderSerializer(orders,many=True)
        return Response(serializer.data)




