from django.urls import include, path

from rest_framework import routers

from paystack.views import transaction, transfer

router = routers.DefaultRouter()
router.register('transaction', transaction.TransactionService)
router.register('transfer', transfer.TransferService)

urlpatterns = [
    path('', include(router.urls)),
]
