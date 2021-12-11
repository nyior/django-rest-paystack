from rest_framework import viewsets
from rest_framework.decorators import action

from paystack.models import TransactionLog
from paystack.serializers import PaymentSerializer
from paystack.services import TransactionService
from paystack.utils import get_authentication_class, return_okay_response


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = TransactionLog.objects.all()
    serializer_class = PaymentSerializer
    http_method_names = ["get", "post"]
    authentication_classes = get_authentication_class()
    lookup_field = "uuid"

    @action(detail=False, methods=["post"])
    def initiate(self, request):
        user_email = request.data.get("email")
        amount = request.data.get("amount")

        payload = {
            "email": user_email if user_email else None,
            "amount": amount * 100 if amount else None,  # price in kobo
            "metadata": {"user_id": request.user.id},
        }

        transaction_service = TransactionService()
        initiated_transaction = transaction_service.initialize_payment(payload)

        return return_okay_response(initiated_transaction)

    @action(detail=False, methods=["get"])
    def verify(self, request):
        transaction_ref = request.query_params.get("transaction_ref")

        paystack_service = TransactionService()
        verified_transaction = paystack_service.verify_payment(transaction_ref)

        return return_okay_response(verified_transaction)

    @action(detail=False, methods=["post"], url_path="charge-customer")
    def charge_customer(self, request):
        user_email = request.data.get("email")
        amount = request.data.get("amount")
        authorization_code = request.data.get("authorization_code")

        payload = {
            "email": user_email if user_email else None,
            "amount": amount * 100 if amount else None,
            "authorization_code": authorization_code if authorization_code else None,
        }

        transaction_service = TransactionService()
        charge = transaction_service.recurrent_charge(payload)

        return return_okay_response(charge)
