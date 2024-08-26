from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_cart_price', 'created_at', 'updated_at')

    def total_cart_price(self, obj):
        return obj.total_cart_price
    total_cart_price.short_description = 'Total Price'



class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'price')
    search_fields = ('product',)
    list_filter = ('cart',)

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
