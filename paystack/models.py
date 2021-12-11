import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class PayStackCustomer(models.Model):
    """
    for charging a customer's card again using authorization code
    for transfers too
    """

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # authorization creds for recurring charges
    email = models.CharField(blank=True, null=True, max_length=100)
    authorization_code = models.CharField(blank=True, null=True, max_length=100)
    card_type = models.CharField(blank=True, null=True, max_length=10)
    last4 = models.CharField(blank=True, null=True, max_length=4)
    exp_month = models.CharField(blank=True, null=True, max_length=10)
    exp_year = models.CharField(blank=True, null=True, max_length=10)
    bin = models.CharField(blank=True, null=True, max_length=10)
    bank = models.CharField(blank=True, null=True, max_length=100)
    account_name = models.CharField(blank=True, null=True, max_length=100)


class TransactionLog(models.Model):

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
    currency = models.CharField(max_length=5)
    txRef = models.CharField(max_length=100, null=True, blank=True)

    payment_date_time = models.DateTimeField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
