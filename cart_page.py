from item_page import ItemPage
from login_page import LoginPage
from selenium import webdriver


class CartPage(LoginPage):
    def __init__(self, driver: webdriver.Chrome, user_name, password):
        LoginPage.__init__(self, driver, user_name, password)

    def navigate(self):
        self.driver.get("https://allegro.pl.allegrosandbox.pl/koszyk")

    # TODO
    def items(self):
        n = len(self.find_many("div._1bo4a._sjrr0._hho8x._1fwkl"))
        for i in range(n)
            pass

    def item_count(self, item_name=None):
        return sum(item.count for item in self.items())

    def compute_total_price(self):
        return sum(item.compute_total_price for item in self.items())

    def add_to_cart(self, item_id, item_count=1):
        item_page = ItemPage(self.driver, self.user_name, self.password, item_id)
        item_page.navigate()
        item_page.quantity_text_box().clear()
        item_page.quantity_text_box().send_keys(str(item_count))
        item_page.add_to_cart_button().click()
        item_page.wait_until_page_loaded()

    # TODO recheck this one
    def remove_item_by_name(self, item_name):
        return self.find("button[data-analytics-interaction-label='remove']")

    # TODO
    def clear(self):
        pass

    # TODO recheck this one
    def increase_item_count(self, item_name):
        return self.find("button[data-analytics-interaction-label='increase']")

    # TODO recheck this one
    def decrease_item_count(self, item_name):
        return self.find("button[data-analytics-interaction-label='decrease']")

    def go_to_checkout_button(self):
        return self.find("button[class='_13q9y._8tsq7._7qjq4']")

    def continue_shopping_button(self):
        return self.find("a[data-analytics-click-label='continueShopping']")
