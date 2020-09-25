from selenium import webdriver
from payment_page import PaymentPage


class PayUPaymentPage(PaymentPage):
    def __init__(self, driver: webdriver.Chrome):
        PaymentPage.__init__(self, driver)

    def do_positive_payment(self):
        self.find("#formSubmit").click()
        self.find("#formSubmit").click()

    def do_negative_payment(self):
        return self.find("#formReturn")

# https://bank-simulator-merch-prod.snd.payu.com/simulator/spring/sandbox/utf8/mbankNew/form
