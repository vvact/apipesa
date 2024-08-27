from django.urls import path
from .views import CartListCreateView, CartDetailView, CartItemListCreateView, CartItemDetailView

urlpatterns = [
    path('cart/', CartListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('cart/items/', CartItemListCreateView.as_view(), name='cart-item-list-create'),
    path('cart/items/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'),
]
