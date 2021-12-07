import pytest

from tests.mixins import URLsMixin, RequestMixin


@pytest.mark.usefixtures(
    "valid_transaction_payload",
    "invalid_transaction_payload"
)
class TestTransactionEndpoints(URLsMixin, RequestMixin):
    
    def test_initiate_transaction(self):
        response = self.send_request(
            request_method='POST',
            request_url=self.initiate_transaction_url(),
            payload=valid_transaction_payload
        )

        assert response.status_code == 200

    def test_initiate_transaction_fails(self):
        response = self.send_request(
            request_method='POST',
            request_url=self.initiate_transaction_url(),
            payload=invalid_transaction_payload
        )

        assert response.status_code != 200
        assert response.status_code != 400

    def test_verify_transaction(self):
        response = self.send_request(
            request_method='GET',
            request_url=self.verify_transaction_url(), # pass transaction ref
        )

        assert response.status_code == 200

    def test_charge_customer(self): # How do I access authorization code here?
        response = self.send_request(
            request_method='POST',
            request_url=self.charge_customer_url(), # pass transaction ref
            payload=valid_transaction_payload
        )

        assert response.status_code == 200

    def test_list_transaction(self):
        response = self.send_request(
            request_method='GET',
            request_url=self.all_transactions_url()
        )

        assert response.status_code == 200