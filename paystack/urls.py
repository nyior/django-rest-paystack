from django.urls import include, path

from rest_framework import routers

from paystack.views import TransactionViewSet, TransferViewSet

router = routers.DefaultRouter()
router.register('transaction', TransactionViewSet)
router.register('transfer', TransferViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
