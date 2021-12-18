import json

import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

User = get_user_model()


class BaseAPIService(object):  # Not to be instantiated directly
    def get_user(self, user_id):
        user = User.objects.get(id=user_id)
        return user

    def make_request(self, method, url, payload=None):

        try:
            PAYSTACK_PRIVATE_KEY = getattr(settings, "PAYSTACK_PRIVATE_KEY")
        except Exception as e:  # If ser hasn't declared variable
            raise ValidationError(e)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer { PAYSTACK_PRIVATE_KEY }",
        }

        response = requests.request(
            method, url, data=json.dumps(payload), headers=headers
        )

        if response.status_code != 200:
            if response.text:
                raise ValidationError(response.text)
            else:
                raise ValidationError(
                    f"paystack failed with error code: {response.status_code}"
                )

        data_json_str = json.dumps(json.loads(response.text))
        # convert json str to json object
        result = json.loads(data_json_str)

        return result

    def validate_amount(self, amount):

        if isinstance(amount, int) or isinstance(amount, float):
            if amount < 0:
                raise ValidationError("Negative amount is not allowed")
            return amount * 100  # in kobo
        else:
            raise ValidationError("Amount must be a number")

    def validate_email(self, email):
        if not email:
            raise ValidationError("Customer Email is required")
