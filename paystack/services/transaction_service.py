from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from paystack.services.base_api_service import BaseAPIService


class TransactionService(BaseAPIService):

    def __init__(self, request) -> None:
        self.request = request
        self.user = request.user

    def _validate_payload(self, payload: dict) -> None:
        """ check that payload has all the required params"""
        required = ["email", "amount"]

        for i in required:
            if not payload[i]:
                raise ValidationError(f"{i} must be provided")

    def initialize_payment(self, payload: dict) -> Response:
        path = "/initialize"

        self._validate_payload(payload)
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