from selenium import webdriver

from home_page import HomePage


class PaymentPage(HomePage):
    def __init__(self, driver: webdriver.Chrome):
        HomePage.__init__(self, driver)

    def positive_payment_result_button(self):
        pass

    def negative_payment_result_button(self):
        pass
