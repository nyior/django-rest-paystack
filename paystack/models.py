import uuid

from djmoney.models.fields import MoneyField
from django.contrib.auth import get_user_model, models

User = get_user_model()


class PayStackCustomer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    metadata = models.JSONField(blank=True, null=True)
    email = models.CharField(blank=True, null=True, max_length=100)
    authorization_code = models.CharField(blank=True, null=True, max_length=100)
    recipient_code = models.CharField(blank=True, null=True, max_length=100)


class BasePaymentHistory(models.Model):

    GATEWAY_PURCHASE = "GATEWAY_PURCHASE"
    TRANSFER = "TRANSFER"

    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    charge_type = models.CharField(
        max_length=30,
        choices=(
            (GATEWAY_PURCHASE, "Gateway Purchase"),
            (TRANSFER, "Transfer"),
        ),
    )
    amount = models.FloatField(max_length=19)
    currency = models.Charfield(max_length=5)
    txRef = models.CharField(max_length=100, null=True, blank=True)

    payment_date_time = models.DateTimeField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
