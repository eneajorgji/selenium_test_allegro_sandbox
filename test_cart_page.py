from unittest import TestCase
from driver import Driver
from cart_page import CartPage
from configuration import USER_NAME, PASSWORD


class TestCartPage(TestCase):

    def setUp(self):
        self.driver = Driver.create()
        self.page = CartPage(self.driver, USER_NAME, PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        self.page.add_to_cart(6442736754, 3)
        self.page.add_to_cart(6500286757)
        self.page.navigate()

        assert self.page.item_count() == 4
        assert self.page.compute_total_price() == 3094.99

    def test_clear_cart(self):
        self.page.add_to_cart(6442736754, 3)
        self.page.navigate()
        self.page.clear_cart()

        assert self.page.item_count() == 0

    def test_clear_after_login(self):
        self.page = CartPage(self.driver, USER_NAME, PASSWORD, True)
        self.page.navigate(should_clear_cart=True)

        assert self.page.item_count() == 0
