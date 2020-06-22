from selenium import webdriver
from home_page import HomePage
from selenium.webdriver.support.ui import Select


class SearchPage(HomePage):  # dziedziczenie z klasy HomePage
    def __init__(self, driver: webdriver.Chrome):
        # super(driver)  # wywoluje instruktora klasy HomePage
        HomePage.__init__(self, driver)

    def search_text_box(self):
        return self.find("input[name=string]")

    def search_combo_box(self):
        return Select(self.find("select._d25db_ZZIhH._1h7wt._k70df.m7er_k4.m7er_wn"))

    def search_button(self):
        return self.find("button._d25db_10Nyi._13q9y._8tsq7._1q2ua")

    def offers_count(self):
        span = self._get_element_if_exists("span._11fdd_39FjG")
        if span:
            return int(span.text.replace(" ", ""))
        span = self._get_element_if_exists("span[data-role='counter-value']")  # find is there is any users
        if span:
            return int(span.text.replace(" ", ""))  # change number from 2 000 to 2000
        return 0

    def has_offers(self):
        return self.offers_count() > 0