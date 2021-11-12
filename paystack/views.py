from django.conf import settings

from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import BasePaymentHistory
from .serializers import PaymentSerializer
from .services.paystack_gateway import PaystackService

from django_rest_paystack.utils import return_okay_response


class PaystackViewSet(viewsets.ModelViewSet):
    queryset = BasePaymentHistory.objects.all()
    serializer_class = PaymentSerializer
    http_method_names = ['get', 'post']
    permission_classes [IsAuthenticated]
    
    @action(detail=False, methods=['post'], name='initialize payment')
    def initialize(self, request):
        user_email = request.user.email
        amount  = request.data['amount'] * 100 # price in kobo
        
        payload  = {
            "email": user_email,
            "amount": amount,
        }
        
        paystack_service = PaystackService(request)
        initiated_transaction = paystack_service.initialize_payment(payload)
       
        return_okay_response(initiated_transaction, status.HTTP_200_OK)

    @action(detail=False, methods=['get'], name='verify payment')
    def verify_payment(self, request):
        transaction_ref  = request.kwargs['transaction_ref']

        paystack_service = PaystackService(request)
        verified_transaction = paystack_service.verify_payment(transaction_ref)
        # Log payment here
       
        return_okay_response(verified_transaction, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], name='validate card')
    def validate_card(self, request):
        card_number = request.kwargs['card_number']

        paystack_service = PaystackService(request)
        response = paystack_service.validate_card(card_number)

        return return_okay_response(response, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], name='validate user bank details')
    def validate_user_bank_details(self, request):
        account_number = request.GET.get('account_number')
        bank_name = request.GET.get('bank_name')

        paystack_service = PaystackService(request)
        response = paystack_service.validate_user_bank_details(
            account_number,
            bank_name
        )

        return_okay_response(response, status=status.HTTP_200_OK)
