from django.contrib import admin

from paystack.models import PayStackCustomer, BasePaymentHistory


class PayStackCustomerAdmin(admin.ModelAdmin):
   model = PayStackCustomer
   list_display = ['user', 'email', 'authorization_code']


class BasePaymentHistoryAdmin(admin.ModelAdmin):
   model = BasePaymentHistory
   list_display = ['uuid', 'user', 'charge_type', 'amount']

admin.site.register(PayStackCustomer, PayStackCustomerAdmin)
admin.site.register(BasePaymentHistory, BasePaymentHistoryAdmin)