import requests, json, os

from django.conf import settings

from rest_framework.exceptions import NotAcceptable
from rest_framework.response import Response


class BaseAPIService(object): # Not to be instantiated directly

    def make_request(method, path, payload=None):
        
        url = "{}{}".format(settings.PAYSTACK_BASE_URL, path)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer { settings.PAYSTACK_PUBLIC_KEY }"
        }

        response = requests.request(
            method, url, data=payload, headers=headers
        )

        data_json_str = json.dumps(json.loads(response.text))

        # convert json str to json object
        result = json.loads(data_json_str)
        
        return result

    def validate_amount(amount):
        if not amount:
            raise NotAcceptable("Amount is required")

        if isinstance(amount, int) or isinstance(amount, float):
            if amount < 0:
                raise NotAcceptable("Negative amount is not allowed")
            return amount
        else:
            raise NotAcceptable("Amount must be a number")

    def validate_email(email):
        if not email:
            raise NotAcceptable("Customer Email is required")