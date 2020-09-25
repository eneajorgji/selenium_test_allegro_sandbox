from home_page import HomePage
import copy


class PaymentCardForm:
    def __init__(self, page: HomePage):
        self.page = copy.copy(page)

    def __enter__(self):
        self.page.driver.switch_to.frame(self.page.find("#payuFrame"))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.page.driver.switch_to.default_content()
        self.page.wait_a_moment()

    def credit_card_number_text_box(self):
        return self.page.find("#cardform_cardNumber")

    def expiry_month_text_box(self):
        return self.page.find("#cardform_cardDateMonth")

    def expiry_year_text_box(self):
        return self.page.find("#cardform_cardDateYear")

    def cvv_text_box(self):
        return self.page.find("#cardform_cardCvv")

    def use_button(self):
        return self.page.find("#cardform_pay")

    def use_credit_card(self, number, year, month, cvv):
        self.credit_card_number_text_box().send_keys(number)
        self.expiry_year_text_box().send_keys(year)
        self.expiry_month_text_box().send_keys(month)
        self.cvv_text_box().send_keys(cvv)
        self.use_button().click()
