from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from apps.cart.models import Cart, CartItem
from apps.cart.utils import calculate_cart_total  # Utility function to calculate total

class CheckoutView(generics.GenericAPIView):
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        session_key = request.session.session_key
        guest_phone_number = request.data.get('guest_phone_number')
        
        if not guest_phone_number:
            return Response({"detail": "Guest phone number is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        cart = Cart.objects.get(session_key=session_key)
        
        # Create Order
        order = Order.objects.create(
            guest_phone_number=guest_phone_number,
            session_key=session_key,
            total_price=calculate_cart_total(cart),
        )

        # Create OrderItems
        cart_items = CartItem.objects.filter(cart=cart)
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                unit_price=cart_item.product.price  # Assuming product has a price attribute
            )

        # Clear cart after order is created
        cart.items.all().delete()

        # Serialize and respond
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

