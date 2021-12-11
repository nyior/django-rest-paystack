import pytest

from tests.mixins import RequestMixin, URLsMixin

pytestmark = pytest.mark.django_db


@pytest.mark.usefixtures(
    "valid_transaction_payload",
    "invalid_transaction_payload",
    "transaction_reference",
    "valid_charge_payload",
    "invalid_charge_payload",
)
class TestTransactionEndpoints(URLsMixin, RequestMixin):
    def test_initiate_transaction(self, valid_transaction_payload):
        response = self.send_request(
            request_method="POST",
            request_url=self.initiate_transaction_url(),
            payload=valid_transaction_payload,
        )

        assert response.status_code == 200

    def test_initiate_transaction_fails(self, invalid_transaction_payload):
        response = self.send_request(
            request_method="POST",
            request_url=self.initiate_transaction_url(),
            payload=invalid_transaction_payload,
        )

        assert response.status_code != 200
        assert response.status_code == 400

    def test_verify_transaction(self, transaction_reference):
        response = self.send_request(
            request_method="GET",
            request_url=self.verify_transaction_url(transaction_reference),
        )

        assert response.status_code == 200

    def test_verify_transaction_fails(self):
        response = self.send_request(
            request_method="GET",
            request_url=self.verify_transaction_url(""),
        )

        assert response.status_code != 200
        assert response.status_code == 400

    def test_charge_customer(self, valid_charge_payload):
        response = self.send_request(
            request_method="POST",
            request_url=self.charge_customer_url(),
            payload=valid_charge_payload,
        )

        assert response.status_code == 200

    def test_charge_customer_fails(self, invalid_charge_payload):
        response = self.send_request(
            request_method="POST",
            request_url=self.charge_customer_url(),
            payload=invalid_charge_payload,
        )

        assert response.status_code != 200
        assert response.status_code == 400

    def test_list_transaction(self):
        response = self.send_request(
            request_method="GET", request_url=self.all_transactions_url()
        )

        assert response.status_code == 200
