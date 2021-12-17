from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from paystack.models import TransactionLog
from paystack.paystack_urls import (
    PAYSTACK_CHARGE_AUTHORIZATION_URL,
    PAYSTACK_INITIALIZE_TRANSACTION_URL,
    PAYSTACK_VERIFY_TRANSACTION_URL,
)

from .base_api_service import BaseAPIService


class TransactionService(BaseAPIService):
    def _create_transaction_object(self, transaction_data):
        user_id = transaction_data["metadata"]["user_id"]
        user = self.get_user(user_id)

        TransactionLog.objects.create(
            user=user,
            charge_type="GATEWAY PURCHASE",
            amount=transaction_data["amount"],
            currency=transaction_data["currency"],
            txRef=transaction_data["reference"],
            payment_date_time=transaction_data["paid_at"],
            status=transaction_data["status"],
        )

    def log_transaction(
        self, transaction_data
    ):  # transaction will be logged in the webhook
        self._create_transaction_object(transaction_data)

    def _validate_initiate_payload(self, payload: dict) -> None:
        """
        check that payload has all the required params
        """
        required = ["email", "amount"]

        for i in required:
            try:
                payload[i]
            except KeyError:
                raise ValidationError(f"{i} must be provided")

        self.validate_amount(payload["amount"])

    def _validate_charge_payload(self, payload: dict) -> None:
        """
        check that payload has all the required params
        """
        required = ["email", "amount", "authorization_code"]

        for i in required:
            try:
                payload[i]
            except KeyError:
                raise ValidationError(f"{i} must be provided")

        self.validate_amount(payload["amount"])

    def initialize_payment(self, payload: dict) -> Response:
        url = PAYSTACK_INITIALIZE_TRANSACTION_URL

        self._validate_initiate_payload(payload)
        return self.make_request("POST", url, payload)

    def verify_payment(self, transaction_ref: str) -> Response:
        url = PAYSTACK_VERIFY_TRANSACTION_URL.format(transaction_ref)

        return self.make_request("GET", url)

    def recurrent_charge(self, payload: dict) -> Response:
        self._validate_charge_payload(payload)

        url = PAYSTACK_CHARGE_AUTHORIZATION_URL

        return self.make_request("POST", url, payload)
