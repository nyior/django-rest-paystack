import pytest

from tests.mixins import RequestMixin, URLsMixin

pytestmark = pytest.mark.django_db


class TestCustomerEndpoints(URLsMixin, RequestMixin):
    def test_list_customers(self):
        response = self.send_request(
            request_method="GET", request_url=self.all_customers_url()
        )

        assert response.status_code == 200
