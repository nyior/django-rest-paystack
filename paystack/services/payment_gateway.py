from abc import ABC, abstractmethod


class PaymentGateway(ABC): # to switch to let's say Flutterwave, we just extend this class

    @abstractmethod
    def initialize_payment(self, paylod: dict)-> None:
        pass
        
    @abstractmethod
    def verify_payment(self, transaction_ref: str) -> None:
        pass

    @abstractmethod
    def validate_card(self):
        pass

    @abstractmethod
    def validate_user_bank_details(
        self, account_number: str, account_name: str, bank_code: str
    ) -> None:
        pass
