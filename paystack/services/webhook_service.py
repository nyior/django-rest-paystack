import hashlib
import hmac
import os

from rest_framework.exceptions import ValidationError

from .customer_service import CustomerService
from .transaction_service import TransactionService


class WebhookService(object):
    def __init__(self, request) -> None:
        self.request = request

    def webhook_handler(self):
        secret = os.environ.get("PAYSTACK_SECRET_KEY")
        webhook_data = self.request.data
        hash = hmac.new(secret, webhook_data, digestmod=hashlib.sha512).hexdigest()

        if hash != self.request.headers["x-paystack-signature"]:
            raise ValidationError("MAC authentication failed")

        if webhook_data["event"] == "charge.success":
            paystack_service = TransactionService()
            paystack_service.log_transaction(webhook_data["data"])

            customer_service = CustomerService()
            customer_service.log_customer(webhook_data["data"])

        return webhook_data
