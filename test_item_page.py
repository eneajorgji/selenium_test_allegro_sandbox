from unittest import TestCase
from driver import Driver
from item_page import ItemPage
from configuration import USER_NAME, PASSWORD


class TestItemPage(TestCase):
    def setUp(self):
        self.driver = Driver.create()

    def tearDown(self):
        self.driver.quit()

    def test_navigate(self):
        self.page = self.__get_item_page(6442736754)
        self.page.navigate()

        assert self.page.item_name() == "Xiaomi Redmi Note 64 GB"
        assert self.page.item_price() == 1000
        assert self.page.cart_item_count() == 0

    def test_add_to_cart_success(self):
        self.page = self.__get_item_page(6442736754)
        self.page.navigate()
        self.page.add_to_cart_button().click()
        self.page.wait_until_page_loaded()

        assert self.page.cart_item_count() == 1

    def test_multiple_add_to_cart_success(self):
        self.page = self.__get_item_page(6442736754)
        self.page.navigate()
        self.page.quantity_text_box().clear()
        self.page.quantity_text_box().send_keys("3")
        self.page.add_to_cart_button().click()
        self.page.wait_until_page_loaded()

        assert self.page.cart_item_count() == 3

    def test_add_to_favorite(self):
        self.page = self.__get_item_page(6442736754, True)
        self.page.navigate()
        self.page.add_to_watch_list_button().click()

        assert self.page.is_added_to_watch_list()

    def __get_item_page(self, id, login_before=False):
        return ItemPage(self.driver, USER_NAME, PASSWORD, id, login_before)
