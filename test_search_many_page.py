from unittest import TestCase
from driver import Driver
from search_many_page import SearchManyPage
from time import time


class TestSearchManyPage(TestCase):
    def setUp(self):
        self.driver = Driver.create()
        self.page = SearchManyPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_search_many_success(self):  # szukaj wiele
        self.page.navigate()
        self.page.search_many_link().click()
        self.page.search_many_input(0).send_keys("telefon")
        self.page.search_many_input(1).send_keys("komputer")
        self.page.search_many_button().click()

        assert self.page.has_multi_offers()

    def test_search_many_five_option_success(self):
        self.page.navigate()
        self.page.search_many_link().click()
        self.page.search_many_input(0).send_keys("telefon")
        self.page.search_many_input(1).send_keys("komputer")

        for i in range(3):
            self.page.search_many_additional_button().click()
            self.page.search_many_input(2 + i).send_keys("aaa")

        self.page.search_many_button().click()
