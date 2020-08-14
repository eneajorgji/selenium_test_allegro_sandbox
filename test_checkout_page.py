from unittest import TestCase
from driver import Driver
from cart_page import CartPage
from configuration import USER_NAME, PASSWORD


class TestCheckoutPage(TestCase):

    def setUp(self):
        self.driver = Driver.create()
        self.page = CartPage(self.driver, USER_NAME, PASSWORD, True)

    def tearDown(self):
        self.driver.quit()

    # TODO trzeba czyszczyc przed dodaniem 3 itemów.
    def test_enumerate_payment_methods(self):
        self.page.navigate(should_clear_cart=True)
        self.page.add_to_cart(6442736754, 3)
        checkout_page = self.page.go_to_checkout_page()
        methods = checkout_page.payment_methods()




