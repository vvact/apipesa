from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from apps.orders.models import Order
import requests
import json
from django.conf import settings

class MpesaPaymentView(APIView):
    def post(self, request, *args, **kwargs):
        order_id = request.data.get('order_id')
        phone_number = request.data.get('phone_number')

        if not order_id or not phone_number:
            return Response({"detail": "Order ID and phone number are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        # Create or update payment record
        payment, created = Payment.objects.get_or_create(order=order, defaults={
            'phone_number': phone_number,
            'amount': order.total_price,
            'status': 'Pending'
        })

        # Prepare payment request payload
        payload = {
            "BusinessShortCode": settings.MPESA_SHORTCODE,
            "Password": settings.MPESA_PASSWORD,
            "Timestamp": settings.MPESA_TIMESTAMP,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": order.total_price,
            "PartyA": phone_number,
            "PartyB": settings.MPESA_SHORTCODE,
            "PhoneNumber": phone_number,
            "CallBackURL": settings.MPESA_CALLBACK_URL,
            "AccountReference": "Order " + str(order.id),
            "TransactionDesc": "Payment for order " + str(order.id)
        }

        headers = {
            "Authorization": "Bearer " + self.get_access_token(),
            "Content-Type": "application/json"
        }

        response = requests.post(settings.MPESA_ENDPOINT, data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            payment.transaction_id = response_data.get('CheckoutRequestID')  # Adjust based on response
            payment.save()
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)

    def get_access_token(self):
        # Get M-Pesa access token
        auth = (settings.MPESA_CONSUMER_KEY, settings.MPESA_CONSUMER_SECRET)
        response = requests.get(settings.MPESA_ACCESS_TOKEN_URL, auth=auth)
        response_data = response.json()
        return response_data.get('access_token')


class PaymentCallbackView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        # Process callback data
        # Verify transaction and update payment status
        # Extract specific information from data and update the payment status

        # Example: Update payment status based on callback data
        try:
            payment = Payment.objects.get(transaction_id=data.get('transaction_id'))
            payment.status = 'Completed'  # Update based on actual callback data
            payment.save()
        except Payment.DoesNotExist:
            return Response({"detail": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)

        return Response({"detail": "Callback received."}, status=status.HTTP_200_OK)

