from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem
from .serializers import CartSerializer
from apps.products.models import Product

class CartView(APIView):
    def get(self, request):
        # Get or create a cart using the session key
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        
        cart, created = Cart.objects.get_or_create(session_key=session_key)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def post(self, request):
        # Add an item to the cart
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key

        cart, created = Cart.objects.get_or_create(session_key=session_key)
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        if product_id and quantity:
            try:
                product = Product.objects.get(id=product_id)
                CartItem.objects.create(cart=cart, product=product, quantity=quantity)
                return Response({'status': 'Item added to cart'}, status=status.HTTP_201_CREATED)
            except Product.DoesNotExist:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Product ID and quantity required'}, status=status.HTTP_400_BAD_REQUEST)
