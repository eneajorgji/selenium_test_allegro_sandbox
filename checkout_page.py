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
        return self.find("input[id='company_78']")

    def address_text_box(self):
        return self.find("input[id='street_65']")

    def post_code_text_box(self):
        return self.find("input[id='zipCode_66']")

    # TODO
    def city_name_text_box(self):
        pass

    def country_combo_box(self):
        return self.find_and_wait_for_clickable("input[name='country']")

    def phone_number_text_box(self):
        return self.find("input[id='phoneNumber_80']")

    # TODO
    def delivery_method_radio_button(self, index):
        pass

    # TODO
    def payment_method_check(self, index):
        pass

    # TODO
    def finalize_button(self):
        pass
