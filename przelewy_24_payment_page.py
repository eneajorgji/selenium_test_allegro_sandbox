from selenium import webdriver
from payment_page import PaymentPage


class Przelewy24PaymentPage(PaymentPage):
    def __init__(self, driver: webdriver.Chrome):
        PaymentPage.__init__(self, driver)

    def do_positive_payment(self):
        self.find("#reagulation-accept-button").click()
        self.find("button[type='submit']").click()
        self.find("#pay_by_link_pay").click()

    def do_negative_payment(self):
        return self.find("a.btn-close")

# https://sandbox.przelewy24.pl/trnRequest/8AB82D0FCD-6EF7AB-FE73BC-4E4DA1B743/243
