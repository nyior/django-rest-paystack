from django.contrib import admin

from paystack.models import PayStackCustomer, TransactionLog


class PayStackCustomerAdmin(admin.ModelAdmin):
    model = PayStackCustomer
    list_display = ["user", "email", "authorization_code"]


class TransactionLogAdmin(admin.ModelAdmin):
    model = TransactionLog
    list_display = ["uuid", "user", "charge_type", "amount"]


admin.site.register(PayStackCustomer, PayStackCustomerAdmin)
admin.site.register(TransactionLog, TransactionLogAdmin)
