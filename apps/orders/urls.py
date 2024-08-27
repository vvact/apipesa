from django.urls import path
from .views import CheckoutView, OrderListCreateView, OrderDetailView, MpesaPaymentView

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('mpesa-payment/', MpesaPaymentView.as_view(), name='mpesa_payment'),
]
