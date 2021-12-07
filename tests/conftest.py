import pytest

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from django.utils.encoding import force_str
from django.contrib.auth import get_user_model

pytestmark = pytest.mark.django_db

User = get_user_model()


@pytest.fixture
@pytest.mark.django_db
def user():
    user, _ = User.objects.get_or_create(
        email="admin@gmail.com", password="Gr3@t!2021"
    )
        
    return 
    

@pytest.fixture
def valid_transaction_payload(user):
    payload  = {
            "email": user.email,
            "amount": 30 * 100,
            "metadata": {
                "user": user
            }
    }

    return payload


@pytest.fixture
def invalid_transaction_payload(user):
    payload  = {
            "email": None,
            "amount": None,
            "metadata": {
                "user": user
            }
    }

    return payload


@pytest.fixture
@pytest.mark.django_db
def client(user):
    token, _ = Token.objects.get_or_create(user=user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token' + token.key)

    return client
