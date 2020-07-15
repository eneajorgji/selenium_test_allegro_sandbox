from selenium import webdriver
from login_page import LoginPage


class ItemPage(LoginPage):
    def __init__(self, driver: webdriver.Chrome, user_name, password, id):
        LoginPage.__init__(self, driver, user_name, password)
        self.id = id

    def navigate(self):
        self.driver.get(f"https://allegro.pl.allegrosandbox.pl/oferta/{self.id}")
        self.accept_button().click()

    def item_name(self):
        return self.find("h1._9a071_1Ux3M._9a071_3nB--._9a071_1R3g4._9a071_1S3No").text

    def item_price(self):
        price_div = self.find("div._9a071_1Q_68")
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

    def remove_item(self):
        return self.find_and_wait_for_clickable("div._9a071_2tnYy._9a071_3I3EK._9a071_Gt_oa._9a071_KEY6j")

    def add_to_watch_list_button(self):
        return self.find("button[data-analytics-interaction-label='AddToWatchList']")

    def remove_from_watch_list_button(self):
        return self.find("button[data-analytics-interaction-label='RemoveFromWatchList']")

    def is_added_to_watch_list(self):
        return self._element_exists("button[data-analytics-interaction-label='RemoveFromWatchList']")

    def buy_now_button(self):
        return self.find("button[id='buy-now-button']")
