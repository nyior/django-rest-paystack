from rest_framework import viewsets

from paystack.models import PayStackCustomer
from paystack.serializers import CustomerSerializer
from paystack.utils import get_authentication_class


class PaystackCustomerViewSet(viewsets.ModelViewSet):
    queryset = PayStackCustomer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ["get"]
    authentication_classes = get_authentication_class()
    lookup_field = "user__id"
