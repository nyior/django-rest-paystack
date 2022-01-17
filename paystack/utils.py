from django.conf import settings
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


def return_okay_response(data=None, status=status.HTTP_200_OK) -> Response:
    response = {"status": "success", "result": data}
    return Response(response, status=status)


def return_bad_response(data, status=status.HTTP_400_BAD_REQUEST) -> Response:
    response = {"status": "Failure", "result": data}
    return Response(response, status=status)


def get_authentication_class():

    try:
        return getattr(settings, "REST_FRAMEWORK")["DEFAULT_AUTHENTICATION_CLASSES"]

    except Exception:
        return (TokenAuthentication,)
