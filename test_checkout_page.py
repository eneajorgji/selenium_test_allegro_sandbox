from unittest import TestCase
from driver import Driver
from cart_page import CartPage
from configuration import USER_NAME, PASSWORD, PRIMARY_PRODUCT_ID, SECONDARY_PRODUCT_ID
from payment_page import PaymentPage
from selenium.webdriver.common.keys import Keys


class TestCheckoutPage(TestCase):

    def setUp(self):
        self.driver = Driver.create()
        self.page = CartPage(self.driver, USER_NAME, PASSWORD, True)

    def tearDown(self):
        self.driver.quit()

    def test_enumerate_payment_methods(self):
        self.page.navigate(should_clear_cart=True)
        self.page.add_to_cart(PRIMARY_PRODUCT_ID, 3)
        self.page.navigate(login_before=False)
        checkout_page = self.page.go_to_checkout_page()
        methods = checkout_page.payment_methods()

        assert len(methods) == 4

    def test_define_credit_card(self):
        self.page.navigate(should_clear_cart=True)
        self.page.add_to_cart(PRIMARY_PRODUCT_ID, 3)
        self.page.navigate(login_before=False)
        checkout_page = self.page.go_to_checkout_page()

        with checkout_page.show_credit_card_form() as form:
            form.use_credit_card("4904623358633921", "25", "02", "548")

        methods = checkout_page.payment_methods()
        assert methods[0].secondary_name.endswith("3921")

    def test_select_installements(self):
        self.page.navigate(should_clear_cart=True)
        self.page.add_to_cart(PRIMARY_PRODUCT_ID, 3)
        self.page.navigate(login_before=False)
        checkout_page = self.page.go_to_checkout_page()
        checkout_page.select_installements(0)
        checkout_page.wait_a_moment()
        checkout_page.finalize_button().click()
        checkout_page.wait_a_moment()

        assert "proces-ratalny" in self.driver.current_url

    def test_buy_using_credit_card(self):
        self.page.navigate(should_clear_cart=True)
        self.page.add_to_cart(PRIMARY_PRODUCT_ID, 3)
        self.page.navigate(login_before=False)

        checkout_page = self.page.go_to_checkout_page()

        with checkout_page.show_credit_card_form() as form:
            form.use_credit_card("4904623358633921", "25", "02", "548")

        checkout_page.finalize_button().click()
        checkout_page.wait_until_page_url_contains("zamowienie")

        assert "dziekujemy" in self.driver.current_url

    def test_buy_using_bank_transfer_v1(self):
        self.page.navigate(should_clear_cart=True)
        self.page.add_to_cart(SECONDARY_PRODUCT_ID, 3)
        self.page.navigate(login_before=False)

        checkout_page = self.page.go_to_checkout_page()
        checkout_page.payment_method_checkbox(2).click()
        checkout_page.wait_a_moment()
        checkout_page.select_bank_radio(0).click()
        checkout_page.finalize_button().click()
        checkout_page.wait_until_page_url_contains("zamowienie")

        payment_page = PaymentPage.from_url(self.driver)
        payment_page.do_positive_payment()
        payment_page.wait_a_moment()

        assert "dziekujemy" in self.driver.current_url

    def test_buy_using_bank_transfer_v2(self):
        self.page.navigate(should_clear_cart=True)
        self.page.add_to_cart(PRIMARY_PRODUCT_ID, 3)
        self.page.navigate(login_before=False)

        checkout_page = self.page.go_to_checkout_page()
        checkout_page.payment_method_checkbox(2).click()
        checkout_page.wait_a_moment()
        checkout_page.select_bank_radio(0).click()
        checkout_page.finalize_button().click()
        checkout_page.wait_until_page_url_contains("zamowienie")

        payment_page = PaymentPage.from_url(self.driver)
        payment_page.do_positive_payment()
        payment_page.wait_a_moment()

        assert "dziekujemy" in self.driver.current_url
