import pytest

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
        
    return user
    

@pytest.fixture
def valid_transaction_payload():
    payload  = {
            "email": user.email,
            "amount": 30 * 100,
    }

    return payload


@pytest.fixture
def invalid_transaction_payload():
    payload  = {
            "email": None,
            "amount": None,
    }

    return payload


@pytest.fixture
def transaction_reference():
    return "1i2r643qy9" # copied from paystack


@pytest.fixture
def valid_charge_payload(user):
    payload  = {
            "email": user.email,
            "amount": 30100,
            "authorization_code": "AUTH_f9q3h9b0g8"
    }

    return payload


@pytest.fixture
def invalid_charge_payload():
    payload  = {
            "email": None,
            "amount": None,
            "authorization_code": ""
    }

    return payload
