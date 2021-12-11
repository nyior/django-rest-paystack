from rest_framework import serializers

from paystack.models import TransactionLog


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionLog
        fields = "__all__"
