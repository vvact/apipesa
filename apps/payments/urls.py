from django.urls import path
from .views import MpesaPaymentView, PaymentCallbackView

urlpatterns = [
    path('mpesa-payment/', MpesaPaymentView.as_view(), name='mpesa_payment'),
    path('mpesa-callback/', PaymentCallbackView.as_view(), name='mpesa_callback'),
]
