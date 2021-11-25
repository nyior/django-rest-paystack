import requests, json, os

from django.conf import settings

from rest_framework.exceptions import ValidationError, NotAcceptable
from rest_framework.response import Response

from base_api_service import BaseAPIService


class TransferService(BaseAPIService):

    def __init__(self, request) -> None:
        self.request = request
        self.user = request.user

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
