import pytest

from paystack.models import PayStackCustomer
from paystack.services import CustomerService
from tests.mock_data import webhook_data

pytestmark = pytest.mark.django_db


class TestCustomerService(CustomerService):
    @pytest.mark.django_db
    def test_log_customer(self):
        self.log_customer(webhook_data)

        assert PayStackCustomer.objects.all().count() > 0
