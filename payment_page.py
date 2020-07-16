from selenium import webdriver

from home_page import HomePage


class PaymentPage(HomePage):
    def __init__(self, driver: webdriver.Chrome):
        HomePage.__init__(self, driver)

    # https://bank-simulator-merch-prod.snd.payu.com/simulator/spring/sandbox/utf8/mbankNew/form

    def positive_payment_result_button(self):
        return self.find("input[id='formSubmit']")

    def negative_payment_result_button(self):
        pass
