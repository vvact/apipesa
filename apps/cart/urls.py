from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.cart.views import CartViewSet

router = DefaultRouter()
router.register(r'cart', CartViewSet)

urlpatterns = [
    path('cart/', include(router.urls)),
]
