# apps/cart/utils.py

from .models import CartItem

def calculate_cart_total(cart):
    """Calculate the total price of all items in the cart."""
    cart_items = CartItem.objects.filter(cart=cart)
    total = sum(item.total_price for item in cart_items)
    return total
