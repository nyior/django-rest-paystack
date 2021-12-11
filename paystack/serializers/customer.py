from rest_framework import serializers

from paystack.models import PayStackCustomer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayStackCustomer
        fields = "__all__"
