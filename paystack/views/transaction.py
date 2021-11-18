from django.conf import settings

from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated

from paystack.models import BasePaymentHistory
from paystack.serializers import PaymentSerializer
from paystack.services.transaction_service import TransactionService

from django_rest_paystack.utils import return_okay_response


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = BasePaymentHistory.objects.all()
    serializer_class = PaymentSerializer
    http_method_names = ['get', 'post']
    permission_classes [IsAuthenticated]
    
    @action(detail=False, methods=['post'], name='initialize payment')
    def initialize(self, request):
        user_email = request.user.email
        amount  = request.data['amount'] * 100 # price in kobo
        
        payload  = {
            "email": user_email if user_email else None,
            "amount": amount if amount else None,
        }

        transaction_service = TransactionService(request)
        initiated_transaction = transaction_service.initialize_payment(payload)
       
        return_okay_response(initiated_transaction, status.HTTP_200_OK)

    @action(detail=False, methods=['get'], name='verify payment')
    def verify_payment(self, request):
        transaction_ref  = request.kwargs['transaction_ref']

        paystack_service = TransactionService(request)
        verified_transaction = paystack_service.verify_payment(transaction_ref)
       
        return_okay_response(verified_transaction, status=status.HTTP_200_OK)