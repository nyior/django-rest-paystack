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
        """
        This is used to charge customers that had already been charged in
        past.
        Expects the payload in the format below:

        {
            "email": "string",
            "amount": float/int,
            "metadata": dict/json, --Optional
        }
        """
        payload = request.data

        if "metadata" in payload:
            payload["metadata"]["user_id"] = request.user.id
        else:
            payload["metadata"] = {"user_id": request.user.id}

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
        """
        This is used to charge customers that had already been charged in
        past.
        Expects the payload in the format below:

        {
            "email": "string",
            "amount": float/int,
            "authorization_code": "string",
        }

        """
        payload = request.data

        transaction_service = TransactionService()
        charge = transaction_service.recurrent_charge(payload)

        return return_okay_response(charge)
