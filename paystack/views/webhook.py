from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view

from paystack.services import WebhookService
from django_rest_paystack.utils import return_okay_response


@csrf_exempt
@api_view()
def webhook_handler(request):
        webhook_service = WebhookService(request)
        webhook_service.webhook_handler()

        return_okay_response()