from rest_framework.response import Response
from rest_framework import status


def return_okay_response(data=None, status=status.HTTP_200_OK):
    response = {"status": "success", "result": data}
    return Response(response, status=status)


def return_bad_response(data, status=status.HTTP_400_BAD_REQUEST):
    response = {"status": "Failure", "result": data}
    return Response(response, status=status)