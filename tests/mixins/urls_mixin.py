from django.urls import reverse


class URLsMixin(object):
    def initiate_transaction_url(self):
        return reverse("transaction-initiate")

    def verify_transaction_url(self, trans_ref):
        return reverse("transaction-verify") + f"?transaction_ref={trans_ref}"

    def charge_customer_url(self):
        return reverse("transaction-charge-customer")

    def transaction_url(self, transaction_id):
        return reverse("transaction-detail")

    def all_transactions_url(self):
        return reverse("transaction-list")

    def webhook_handler_url(self):
        return reverse("webhook-handler")

    def get_customer_url(self, user_id):
        return reverse("customer-detail")

    def all_customers_url(self):
        return reverse("customer-list")
