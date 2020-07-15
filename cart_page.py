from login_page import LoginPage
from selenium import webdriver


class CartPage(LoginPage):
    def __init__(self, driver: webdriver.Chrome, user_name, password):
        LoginPage.__init__(self, driver, user_name, password)

    # TODO
    def items(self):
        pass

    def item_count(self, item_name=None):
        return sum(item.count for item in self.items())

    def compute_total_price(self):
        return sum(item.compute_total_price for item in self.items())

    def remove_item_by_name(self, item_name):
        return self.find("button[data-analytics-interaction-label='remove']")

    # TODO
    def clear(self):
        pass

    def increase_item_count(self, item_name):
        return self.find("button[data-analytics-interaction-label='increase']")

    def decrease_item_count(self, item_name):
        return self.find("button[data-analytics-interaction-label='decrease']")

    def go_to_checkout_button(self):
        return self.find("button[class='_13q9y._8tsq7._7qjq4']")

    def continue_shopping_button(self):
        return self.find("a[data-analytics-click-label='continueShopping']")
