import pytest
from rest_framework.exceptions import ValidationError

from paystack.models import TransactionLog
from paystack.services import TransactionService
from tests.mock_data import webhook_data

pytestmark = pytest.mark.django_db


class TestTransactionService(TransactionService):
    @pytest.mark.django_db
    def test_log_transaction(self):
        self.log_transaction(webhook_data)

        assert TransactionLog.objects.all().count() > 0

    def test_validate_initiate_transaction_payload(self, invalid_transaction_payload):
        with pytest.raises(ValidationError):
            self._validate_initiate_payload(invalid_transaction_payload)

    def test_validate_charge_payload(self, invalid_charge_payload):
        with pytest.raises(ValidationError):
            self._validate_charge_payload(invalid_charge_payload)
