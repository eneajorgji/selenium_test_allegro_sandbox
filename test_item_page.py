from unittest import TestCase
from driver import Driver
from search_page import SearchPage
from item_page import ItemPage
from home_page import HomePage
from time import time

class TestItemPage(TestCase):
    def setUp(self):
        self.driver = Driver.create()

    def tearDown(self):
        self.driver.quit()

    def test_navigate(self):
        self.page = self.__get_item_page(6442736754)
        self.page.navigate()

    def __get_item_page(self, id):
        return ItemPage(self.driver, id)

    def test_add_to_cart_success(self):
        self.page = self.__get_item_page(6442736754)
        self.page.navigate()
        self.page.add_to_chart_label().click()

        assert self.page.added_to_chart_label()

    def test_multiple_add_to_cart_success(self):
        self.page = self.__get_item_page(6442736754)
        self.page.navigate()

        for item in range(5):
            self.page.add_another_item().click()

        for item in range(2):
            self.page.remove_item().click()

        self.page.add_to_chart_label().click()

        assert self.page.added_to_chart_label()

    def test_add_to_favorite(self):
        self.page = self.__get_item_page(6442736754)
        self.page.navigate()
        self.page.search_button_favorite().click()
        self.page.tim().sleep(10)