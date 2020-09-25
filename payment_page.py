from abc import ABC, abstractmethod
from selenium import webdriver
from home_page import HomePage


class PaymentPage(ABC, HomePage):
    def __init__(self, driver: webdriver.Chrome):
        HomePage.__init__(self, driver)

    @abstractmethod
    def do_positive_payment(self):
        pass

    @abstractmethod
    def do_negative_payment(self):
        pass

    @staticmethod
    def from_url(driver: webdriver.Chrome):
        url = driver.current_url
        if "payu.com" in url:
            from payu_payment_page import PayUPaymentPage
            return PayUPaymentPage(driver)
        if "przelewy24" in url:
            from przelewy_24_payment_page import Przelewy24PaymentPage
            return Przelewy24PaymentPage(driver)
        raise ValueError(f"Niepoprawny URL:{url}")
