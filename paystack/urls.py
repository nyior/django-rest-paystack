from django.urls import include, path
from rest_framework import routers

from paystack.views import (PaystackCustomerViewSet, TransactionViewSet,
                            webhook_handler)

router = routers.DefaultRouter()
router.register("transaction", TransactionViewSet, basename="transaction")
router.register("paystack-customer", PaystackCustomerViewSet, basename="customer")

urlpatterns = [
    path("", include(router.urls)),
    path("webook-handler", webhook_handler, name="webhook-handler"),
]
