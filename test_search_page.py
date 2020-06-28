from unittest import TestCase
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
        self.page.search_text_box().send_keys("Telefon")
        self.page.search_button().click()

        assert self.page.has_offers()

    def test_search_fail(self):
        self.page.navigate()
        self.page.search_text_box().send_keys("aaabb")
        self.page.search_button().click()

        assert not self.page.has_offers()

    def test_search_success_category(self):
        self.page.navigate()
        self.page.search_text_box().send_keys("Laptop")
        self.page.search_combo_box().select_by_value("/kategoria/elektronika")
        self.page.search_button().click()

        assert self.page.has_offers()

    def test_fail_category(self):
        self.page.navigate()
        self.page.search_text_box().send_keys("aaaabbbb")
        self.page.search_combo_box().select_by_value("/kategoria/elektronika")
        self.page.search_button().click()

        assert not self.page.has_offers()

    def test_search_user_fail(self):
        self.page.navigate()
        self.page.search_text_box().send_keys("Janusz Selenium")
        self.page.search_combo_box().select_by_visible_text("Użytkownicy")
        self.page.search_button().click()

        assert self.page.is_user_not_found()

    def test_search_user_success(self):
        self.page.navigate()
        self.page.search_text_box().send_keys("janusz")
        self.page.search_combo_box().select_by_visible_text("Użytkownicy")
        self.page.search_button().click()

        assert not self.page.has_offers()

    # def test_search_many_success(self):  # szukaj wiele
    #     self.page.navigate()
    #     self.page.search_many_link().click()
    #     self.page.search_many_input(0).send_keys("telefon")
    #     self.page.search_many_input(1).send_keys("komputer")
    #     self.page.search_many_button().click()
    #
    #     assert self.page.has_multi_offers()
    #
    # def test_search_many_five_option_success(self):
    #     self.page.navigate()
    #     self.page.search_many_link().click()
    #     self.page.search_many_input(0).send_keys("telefon")
    #     self.page.search_many_input(1).send_keys("komputer")
    #     for i in range(3):
    #         self.page.search_many_additional_button().click()
    #         self.page.search_many_input(2 + i).send_keys("aaa")
