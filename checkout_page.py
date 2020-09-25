from selenium import webdriver
from configuration import ELEMENT_NOT_FOUND_EXCEPTION
from login_page import LoginPage
from payment_card_form import PaymentCardForm
from payment_method import PaymentMethod


class CheckoutPage(LoginPage):
    def __init__(self, driver: webdriver.Chrome, user_name, password, login_before=False):
        LoginPage.__init__(self, driver, user_name, password)
        self.login_before = login_before
        self.accept_another_buy()

    def accept_another_buy(self):
        try:
            button = self.find("button[ng-click='$ctrl.confirm()']")
            button.click()
        except ELEMENT_NOT_FOUND_EXCEPTION:
            pass

    def payment_methods(self):
        result = []
        paragraphs = self.find_many("div[ng-if] p.m-type--small")
        secondary_paragraphs = self.find_many("div[ng-if] p.m-type--small + p")
        index = 0
        for paragraph, secondary_paragraphs in zip(paragraphs, secondary_paragraphs):
            method = PaymentMethod()
            method.index = index
            method.name = paragraph.text
            method.secondary_name = secondary_paragraphs.text
            result.append(method)
            index += 1
        return result

    def payment_method_checkbox(self, index):
        paragraphs = self.find_many("div[ng-if] p.m-type--small")
        return paragraphs[index]

    def select_bank_radio(self, index):
        radios = self.find_many("label.m-choice--align-middle")
        return radios[index]

    def show_credit_card_form(self):
        self.payment_method_checkbox(0).click()
        form = PaymentCardForm(page=self)
        return form

    def select_installements(self, plan_index):
        self.payment_method_checkbox(3).click()
        self.installements_confirm_button().click()
        self.select_installements_plan(plan_index)

    def select_installements_plan(self, index):
        check_boxes = self.find_many("m-soap[mmessageid='installments-limit-message']")
        check_boxes[index].click()

    def installements_confirm_button(self):
        return self.find("button.m-button--primary[ng-click='modal.confirmSelection()']")

    def finalize_button(self):
        if self._element_exists("buy-button-label"):
            return self.find("buy-button-label")
        return self.find("ng-transclude span")
