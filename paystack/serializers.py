from rest_framework import serializers

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransactionIntent
        fields = '__all__'
        read_only_fields = ( 'date_created' )
