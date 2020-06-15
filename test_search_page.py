from unittest import TestCase

from selenium.webdriver.common.keys import Keys

from driver import Driver
from search_page import SearchPage


class TestSearchPage(TestCase):

    def setUp(self):
        self.driver = Driver.create()
        self.page = SearchPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_search_success(self):
        self.page.navigate()
        self.page.accept_button()
        self.page.search_text_box().send_keys("Telefon" + Keys.ENTER)
        self.page.search_button().click()

        assert self.page.has_offers()

    def test_search_fail(self):
        pass
