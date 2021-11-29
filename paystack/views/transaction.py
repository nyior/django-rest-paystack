from django.conf import settings

from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated

from paystack.models import BasePaymentHistory
from paystack.serializers import PaymentSerializer
from paystack.services import TransactionService, transaction_service

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
        }

        transaction_service = TransactionService(request)
        initiated_transaction = transaction_service.initialize_payment(payload)
       
        return_okay_response(initiated_transaction)

    @action(detail=False, methods=['get'], name='verify payment')
    def verify_payment(self, request):
        transaction_ref  = request.kwargs['transaction_ref']

        paystack_service = TransactionService(request)
        verified_transaction = paystack_service.verify_payment(transaction_ref)
       
        return_okay_response(verified_transaction)

    @action(detail=False, methods=['get'], name='all transactions')
    def transactions(self, request):
        data = {
            'pagination' : request.GET.get('pagination', 10),
            'start_date' : request.GET.get('start_date', None),
            'end_date' : request.GET.get('end_date', None),
            'status' : request.GET.get('status', None),
        }

        paystack_service = TransactionService(request)
        all_transactions = paystack_service.transactions(**data)
       
        return_okay_response(all_transactions)

    @action(detail=False, methods=['get'], name='single transaction')
    def transaction(self, request):
        transaction_id = request.kwargs['transaction_id']

        paystack_service = TransactionService(request)
        transaction = paystack_service.transaction(transaction_id)
       
        return_okay_response(transaction)


    