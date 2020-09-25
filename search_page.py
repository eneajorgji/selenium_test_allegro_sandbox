from selenium import webdriver
from home_page import HomePage
from selenium.webdriver.support.ui import Select
import re


class SearchPage(HomePage):
    def __init__(self, driver: webdriver.Chrome):
        HomePage.__init__(self, driver)

    def search_text_box(self):
        return self.find("input[name=string]")

    def search_combo_box(self):
        return Select(self.find("select[data-role='filters-dropdown-toggle']"))

    def search_button(self):
        return self.find("button[data-role='search-button']")

    def offers_count(self):
        text = self._page_text()
        match = re.search(r"(\d+) ofert", text)
        if match:
            return int(match.group(1))
        return 0

    def has_offers(self):
        return self.offers_count() > 0
