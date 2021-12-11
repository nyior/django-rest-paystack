import requests, json, os

from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework.exceptions import ValidationError

User = get_user_model()


class BaseAPIService(object): # Not to be instantiated directly

    def get_user(self, user_id):
        return User.objects.get(id=user_id)

    def make_request(self, method, url, payload=None):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ.get('PAYSTACK_PRIVATE_KEY')}"
        }

        response = requests.request(
            method, 
            url, 
            data=json.dumps(payload), 
            headers=headers
        )

        if response.status_code != 200:
            if response.text:
                raise ValidationError(
                    response.text
                )
            else:
                raise ValidationError(
                    f"paystack failed with error code: {response.status_code}"
                )  
                
        data_json_str = json.dumps(json.loads(response.text))
        # convert json str to json object
        result = json.loads(data_json_str)
        
        return result
       
    def validate_amount(self, amount):
        if not amount:
            raise ValidationError("Amount is required")

        if isinstance(amount, int) or isinstance(amount, float):
            if amount < 0:
                raise ValidationError("Negative amount is not allowed")
            return amount
        else:
            raise ValidationError("Amount must be a number")

    def validate_email(self, email):
        if not email:
            raise ValidationError("Customer Email is required")