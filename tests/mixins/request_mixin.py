import pytest
import json

from django.utils.encoding import force_str
from django.contrib.auth import get_user_model

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


pytestmark = pytest.mark.django_db

User = get_user_model()


@pytest.mark.usefixtures("client")
class RequestMixin(object):
    
    @pytest.mark.django_db
    def _client(self):
        user, _ = User.objects.get_or_create(
            email="admin@gmail.com", password="Gr3@t!2021"
        )

        token, _ = Token.objects.get_or_create(user=user)

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        print(f"token={token.key}")

        return client

    def send_request(self, **kwargs):
        request_method = kwargs.get('request_method').lower()
        request_url  =   kwargs.get('request_url')
        
        client = self._client()
        if  request_method == "post":
            response = client.post(
                request_url,
                data=kwargs['payload'],
                format='json'
            )
            
        if request_method == "get":
            response = client.get(
                request_url
            )
        
        return response