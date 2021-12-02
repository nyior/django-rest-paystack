from rest_framework import viewsets
from rest_framework.decorators import action
from paystack.services import webhookService

from django_rest_paystack.utils import return_okay_response
from paystack.services import WebhookService


class WebhookView(viewsets.ModelViewSet):
    http_method_names = ['post']
    
    @action(detail=False, methods=["post"])
    def webhook_handler(self, request):
        webhook_service = WebhookService(request)
        webhook_service.webhook_handler()

        return_okay_response()