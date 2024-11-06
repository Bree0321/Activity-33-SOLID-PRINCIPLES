class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Process payment using credit card details
        pass

class PaypalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount, token):
        # Process payment using Paypal token
        pass