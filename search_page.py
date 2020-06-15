from selenium import webdriver

from home_page import HomePage


class SearchPage(HomePage):  # dziedziczenie z klasy HomePage
    def __init__(self, driver: webdriver.Chrome):
        # super(driver)  # wywoluje instruktora klasy HomePage
        HomePage.__init__(self, driver)

    def search_text_box(self):
        return self.find("input[name=string]")

    def search_combo_box(self):
        return self.find("select._d25db_ZZIhH._1h7wt._k70df.m7er_k4.m7er_wn")

    def search_button(self):
        return self.find("button._d25db_10Nyi._13q9y._8tsq7._1q2ua")

    def offers_count(self):
        span = self.find("span._11fdd_39FjG")
        return int(span.text.replace(" ", ""))

    def has_offers(self):
        return self.offers_count() > 0
