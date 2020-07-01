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
        return self.find("#add-to-cart-button")

    def added_to_chart_label(self):
        return self.find("button._13q9y._8hkto.mp7g_f6.mnjl_0.mg9e_0.mvrt_0.mj7a_0.mh36_0.mg9e_0.mvrt_0.mj7a_0.mh36_0.mt3o_0")

    def add_another_item(self):
        return self.find("button._9a071_2tnYy._9a071_3I3EK._9a071_gW37L._9a071_3H9tX")

    def buy_now_label(self):
        pass

    def numbers_of_items_label(self):
        pass
