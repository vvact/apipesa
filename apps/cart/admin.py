from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    fields = ('product', 'quantity', 'price', 'get_total_price')
    readonly_fields = ('price', 'get_total_price')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'session_key','get_total_price', 'created_at')
    search_fields = ('user__username', 'session_key')
    inlines = [CartItemInline]

    def get_total_price(self, obj):
        return obj.get_total_price()
    get_total_price.short_description = 'Total Price'

    def total_price_display(self, obj):
        return obj.get_total_price()
    total_price_display.short_description = 'Total Price'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity', 'added_at')
    search_fields = ('cart__id', 'product__name')
