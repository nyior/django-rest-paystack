import uuid

from djmoney.models.fields import MoneyField
from django.contrib.auth import get_user_model, models

User = get_user_model()


class PayStackCustomer(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    metadata = models.JSONField(blank=True, null=True)
    paystack_id = models.CharField(blank=True, null=True, max_length=100)
    authorization_code = models.CharField(blank=True, null=True, max_length=100)
    recipient_code = models.CharField(blank=True, null=True, max_length=100)


class BasePaymentHistory(models.Model):

    GATEWAY_PURCHASE = "GATEWAY_PURCHASE"
    CASH_REVERSAL = "CASH_REVERSAL"
    TRANSFER = "TRANSFER"

    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    charge_type = models.CharField(
        max_length=30,
        choices=(
            (GATEWAY_PURCHASE, "Gateway Order Purchase"),
            (CASH_REVERSAL, "Cash Reversal"),
            (TRANSFER, "Transfer"),
        ),
    )
    amount = MoneyField(max_digits=19, decimal_places=4, default_currency="NGN")

    txRef = models.CharField(max_length=100, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)

    payment_date_time = models.DateTimeField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
