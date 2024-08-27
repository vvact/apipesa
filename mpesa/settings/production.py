from . base import *


# M-Pesa settings
# MPESA_CONSUMER_KEY = 'your_consumer_key'
# MPESA_CONSUMER_SECRET = 'your_consumer_secret'
# MPESA_SHORTCODE = 174379
# MPESA_PASSWORD = 'Safaricom999!*!'
# MPESA_TIMESTAMP = 'current_timestamp'  # You may need to dynamically generate this
# MPESA_ENDPOINT = 'https://sandbox.safaricom.co.ke/mpesa/charity/v1/safaricom-safaricom'
# MPESA_ACCESS_TOKEN_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
# MPESA_CALLBACK_URL = 'http://yourdomain.com/api/mpesa-callback/'



REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'django_filters.rest_framework.OrderingFilter',
        'filters.SearchFilter',
        'filters.CustomFilterBackend',
        ],
}
