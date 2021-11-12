import requests, json, os

from django.shortcuts import get_object_or_404
from django.conf import settings

from rest_framework.exceptions import ValidationError, NotAcceptable
from rest_framework.response import Response
from rest_framework import status

from .payment_gateway import PaymentGateway


class PaystackService(PaymentGateway):

    def __init__(self, request) -> None:
        self.request = request
        self.user = request.user

    def _paystack_connector(http_method, path, payload=None):

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer { settings.PAYSTACK_PUBLIC_KEY }"
        }

        url = settings.PAYSTACK_BASE_URL + path

        response = requests.request(
            http_method, url, data=payload, headers=headers
        )

        data_json_str = json.dumps(json.loads(response.text))

        # convert json str to json object
        result = json.loads(data_json_str)
        
        return result

    def initialize_payment(self, payload: dict) -> Response:
        path = "/initialize"
        response = self._paystack_connector("POST", path, payload)

        return response

    def verify_payment(self, transaction_ref: str) -> Response:
        path = "/verify/{0}".format(transaction_ref)
        
        response = self._paystack_connector("GET", path)
       
        if response.data["status"] == "success" and response.status_code == 200:
            return response
            # log transaction here
        else:
            raise ValidationError("payment for this transaction could not be processed")

    def validate_card(self, card_number: str) -> Response: 
        last_6 = card_number[-6:]
        path = "/decision/bin/{0}".format(last_6)

        response = self._paystack_connector("POST", path)

        if not response["status"] and not response.status_code == 200:
          raise ValidationError("This card is invalid")
        else:
            return response

    def validate_user_bank_details(
        self, account_number, bank_name
    ) -> Response:     
        bank_name = bank_name
        account_number = account_number
        bank_code = " "
        
        path = "/bank/resolve?account_number={0}&bank_code={1}".format(
            account_number, bank_code
        )

        response = self._paystack_connector("POST", path)

        if not response["status"] and not response.status_code == 200:
          raise ValidationError("This card is invalid")
        else:
            return response
