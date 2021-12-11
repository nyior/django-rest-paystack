from paystack.models import PayStackCustomer

from .base_api_service import BaseAPIService


class CustomerService(BaseAPIService):
    def _create_customer_object(self, user, customer_data, authorization_data):
        defaults = {
            "user": user,
            "email": customer_data["email"],
            "authorization_code": authorization_data["authorization_code"],
            "card_type": authorization_data["card_type"],
            "last4": authorization_data["last4"],
            "exp_month": authorization_data["exp_month"],
            "exp_year": authorization_data["exp_year"],
            "bin": authorization_data["bin"],
            "bank": authorization_data["bank"],
            "account_name": authorization_data["account_name"],
        }

        PayStackCustomer.objects.update_or_create(**defaults, defaults=defaults)

    def log_customer(self, webhook_data) -> None:
        user_id = webhook_data["metadata"]["user_id"]
        user = self.get_user(user_id)

        customer_data = webhook_data["customer"]
        authorization_data = webhook_data["authorization"]

        self._create_customer_object(user, customer_data, authorization_data)
