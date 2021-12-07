from django.urls import include, path

from rest_framework import routers

from paystack.views import TransactionViewSet, PaystackCustomerViewSet, webhook_handler

router = routers.DefaultRouter()
router.register('transaction', TransactionViewSet)
router.register('paystack-customer', PaystackCustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('webook-handler', webhook_handler, name='webhook-handler'),
]
