from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated

from paystack.models import BasePaymentHistory
from paystack.serializers import PaymentSerializer
from paystack.services import TransactionService

from django_rest_paystack.utils import return_okay_response


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = BasePaymentHistory.objects.all()
    serializer_class = PaymentSerializer
    http_method_names = ['get', 'post']
    permission_classes [IsAuthenticated]
    lookup_field = 'uuid'
    
    @action(detail=False, methods=['post'], name='initialize payment')
    def initialize(self, request):
        user_email = request.user.email
        amount  = request.data['amount'] * 100 # price in kobo
        
        payload  = {
            "email": user_email if user_email else None,
            "amount": amount if amount else None,
            "metadata": {
                "user": request.user
            }
        }

        transaction_service = TransactionService(request)
        initiated_transaction = transaction_service.initialize_payment(payload)
       
        return_okay_response(initiated_transaction)

    @action(detail=False, methods=['get'], name='verify payment')
    def verify_transaction(self, request):
        transaction_ref  = request.kwargs['transaction_ref']

        paystack_service = TransactionService(request)
        verified_transaction = paystack_service.verify_payment(transaction_ref)
       
        return_okay_response(verified_transaction)

    @action(detail=False, methods=['post'], name='recurrent_charge')
    def recurrent_charge(self, request):
        user_email = request.user.email
        amount  = request.data['amount'] * 100 # price in kobo
        auth_code = request.data['auth_code']
        
        payload  = {
            "email": user_email if user_email else None,
            "amount": amount if amount else None,
            "auth_code": auth_code if auth_code else None,
        }

        transaction_service = TransactionService(request)
        charge = transaction_service.recurrent_charge(payload)
       
        return_okay_response(charge)

    