from django.conf import settings

from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated

from paystack.models import BasePaymentHistory
from paystack.services.transfer_service import TransferService

from django_rest_paystack.utils import return_okay_response


class TransferViewSet(viewsets.ModelViewSet):
    queryset = BasePaymentHistory.objects.all()
    http_method_names = ['get', 'post']
    permission_classes [IsAuthenticated]

    @action(detail=False, methods=['get'], name='validate card')
    def validate_card(self, request):
        card_number = request.kwargs['card_number']

        paystack_service = TransferService(request)
        response = paystack_service.validate_card(card_number)

        return return_okay_response(response, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], name='validate user bank details')
    def validate_user_bank_details(self, request):
        account_number = request.GET.get('account_number')
        bank_name = request.GET.get('bank_name')

        paystack_service = TransferService(request)
        response = paystack_service.validate_user_bank_details(
            account_number,
            bank_name
        )

        return_okay_response(response, status=status.HTTP_200_OK)
