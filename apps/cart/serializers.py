# serializers.py
from rest_framework import serializers
from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()
    price = serializers.ReadOnlyField(source='product.price')

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'price', 'quantity', 'subtotal', 'added_at']

    def get_subtotal(self, obj):
        return obj.get_total_price()

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'items', 'session_key', 'created_at', 'updated_at', 'total_price']

    def get_total_price(self, obj):
        return obj.get_total_price()
