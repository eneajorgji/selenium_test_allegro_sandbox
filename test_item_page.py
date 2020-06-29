from unittest import TestCase
from driver import Driver
from search_page import SearchPage
from item_page import ItemPage


class TestItemPage(TestCase):
    def setUp(self):
        self.driver = Driver.create()

    def tearDown(self):
        self.driver.quit()

    def test_navigate(self):
        page = self.__get_item_page(6442736754)
        page.navigate()

    def __get_item_page(self, id):
        return ItemPage(self.driver, id)
