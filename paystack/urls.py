from django.urls import include, path
from rest_framework import routers

from paystack.views import PaystackCustomerViewSet, TransactionViewSet, WebhookView

router = routers.DefaultRouter()
router.register("transaction", TransactionViewSet, basename="transaction")
router.register("paystack-customer", PaystackCustomerViewSet, basename="customer")

urlpatterns = [
    path("", include(router.urls)),
    path("webook-handler", WebhookView.as_view(), name="webhook-handler"),
]
