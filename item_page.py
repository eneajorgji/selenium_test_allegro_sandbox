from selenium import webdriver
from login_page import LoginPage


class ItemPage(LoginPage):
    def __init__(self, driver: webdriver.Chrome, user_name, password, id, login_before=False):
        LoginPage.__init__(self, driver, user_name, password)
        self.id = id
        self.login_before = login_before

    def item_name(self):
        return self.find("div[data-role='app-container'] h1").text

    def item_price(self):
        price_div = self.find("div[data-role='app-container'] div[aria-label]")
        return float(price_div.text.replace(" ", "").replace("zł", "").replace(",", "."))

    def cart_item_count(self):
        quantity_div = self.find("div[data-role='cart-quantity']")
        if quantity_div.text:
            return int(quantity_div.text)
        return 0

    def add_to_cart_button(self):
        return self.find("#add-to-cart-button")

    def continue_shopping_button(self):
        return self.find("button[data-analytics-interaction-label='continueShopping']")

    def go_to_cart_button(self):
        return self.find("a[data-analytics-interaction-label='goToCart']")

    def quantity_text_box(self):
        return self.find("input[name='quantity']")

    def add_to_watch_list_button(self):
        return self.find("button[data-analytics-interaction-label='AddToWatchList']")

    def remove_from_watch_list_button(self):
        return self.find("button[data-analytics-interaction-label='RemoveFromWatchList']")

    def is_added_to_watch_list(self):
        return self._element_exists("button[data-analytics-interaction-label='RemoveFromWatchList']")

    def buy_now_button(self):
        return self.find("button[id='buy-now-button']")

    def _on_before_navigate(self):
        if self.login_before:
            self.login()

    def _on_just_navigate(self):
        self.driver.get(f"https://allegro.pl.allegrosandbox.pl/oferta/{self.id}")
