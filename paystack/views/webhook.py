from rest_framework.views import APIView

from paystack.services import WebhookService
from paystack.utils import return_okay_response


class WebhookFacadeView(APIView):
    """
    Exsits for extensibility reasons. Users might want to capture
    the data returned from Paystack and do some stuff with it.
    E.g  retrieve the user tied to the
    payment(usually passed as a meta data in this package)
    and clear the user's cart or create an order for that user.
    """

    authentication_classes = []
    permission_classes = []

    def post(self, request):
        webhook_service = WebhookService(request)
        return (
            webhook_service.webhook_handler()
        )  # This returns raw JSON data from Paystack


class WebhookView(WebhookFacadeView):
    def post(self, request):
        webhook_data = super().post(request)

        return_okay_response(webhook_data)  # Return instance of JsonResponse
