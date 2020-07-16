from selenium import webdriver

from login_page import LoginPage


class CheckoutPage(LoginPage):
    def __init__(self, driver: webdriver.Chrome, user_name, password):
        LoginPage.__init__(self, driver, user_name, password)

    def first_name_text_box(self):
        return self.find("input[id='firstName_74']")

    def last_name_text_box(self):
        return self.find("input[id='lastName_76']")

    def company_name_text_box(self):
        return self.find("input[id='']")

    def address_text_box(self):
        pass

    def post_code_text_box(self):
        pass

    def street_name_text_box(self):
        pass

    def country_combo_box(self):
        pass

    def phone_number_text_box(self):
        pass

    def delivery_method_radio_button(self, index):
        pass

    def payment_method_check(self, index):
        pass

    def finalize_button(self):
        pass
