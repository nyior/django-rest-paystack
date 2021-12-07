from django.urls import reverse


class URLsMixin(object):
    
    def __init__(self):
        pass

    def initiate_transaction_url(self):
        return reverse('initiate-transaction')

    def verify_transaction_url(self, trans_ref):
        return reverse('verify-transaction')+ f"?transaction_ref={trans_ref}"

    def charge_customer_url(self):
        return reverse('charge-customer')

    def transaction_url(self, transaction_id):
        return reverse('transaction-detail')
    
    def all_transactions_url(self):
        return reverse('transaction-list')

    def webhook_handler_url(self):
        return reverse('webhook-handler')

    def get_customer_url(self, user_id):
        return reverse('paystack-customer-detail')
        
    def all_customers_url(self):
        return reverse('paystack-customer-list')
        
