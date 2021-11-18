from rest_framework import serializers

from paystack.models import BasePaymentHistory

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasePaymentHistory
        fields = '__all__'
