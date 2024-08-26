from django.db import models
from apps.products.models import Product
from django.utils import timezone

class Cart(models.Model):
    session_key = models.CharField(max_length=40, unique=True,default='default_session_key')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart with session key {self.session_key}"
    
    def get_total_price(self):
        total = sum(item.get_total_price() for item in self.items.all())
        return total
    

class CartItem(models.Model):

    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Cart"
    
    def get_total_price(self):
        return self.quantity * self.product.price
    
    @property
    def price(self):
        return self.product.price
