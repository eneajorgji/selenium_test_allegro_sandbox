from selenium import webdriver

from home_page import HomePage


class ItemPage(HomePage):
    def __init__(self, driver: webdriver.Chrome, id):  # id item
        HomePage.__init__(self, driver)
        self.id = id

    def navigate(self):
        self.driver.get(f"https://allegro.pl.allegrosandbox.pl/oferta/{self.id}")
        self.accept_button().click()

    def title_label(self):
        pass

    def price_label(self):
        pass

    def delivery_label(self):
        pass

    def return_label(self):
        pass

    def add_to_chart_label(self):
        pass

    def buy_now_label(self):
        pass

    def numbers_of_items_label(self):
        pass
