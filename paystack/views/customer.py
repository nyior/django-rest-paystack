from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from paystack.models import PayStackCustomer
from paystack.serializers import CustomerSerializer


class PaystackCustomerViewSet(viewsets.ModelViewSet):
    queryset = PayStackCustomer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    lookup_field = 'user__id'
    
    