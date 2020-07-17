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
        self.page.navigate()

        assert self.page.item_count() == 1
