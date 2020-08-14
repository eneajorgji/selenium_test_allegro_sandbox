from cart_item import CartItem
from checkout_page import CheckoutPage
from item_page import ItemPage
from login_page import LoginPage
from selenium import webdriver


# TODO czyszczenie koszyka po zalogowaniu
class CartPage(LoginPage):
    def __init__(self, driver: webdriver.Chrome, user_name, password, login_before=False):
        LoginPage.__init__(self, driver, user_name, password)
        self.login_before = login_before
        self.should_clear_cart = False

    def navigate(self, **kwargs):
        if "should_clear_cart" in kwargs:
            self.should_clear_cart = kwargs["should_clear_cart"]
        LoginPage.navigate(self)

    def items(self):
        result = []
        anchors = self.find_many("offer-title a._w7z6o._uj8z7")
        inputs = self.find_many("input[data-box-name='number-picker']")
        spans = self.find_many("offer-row price div._1svub._1k8lh")
        index = 0
        for anchor, input, span in zip(anchors, inputs, spans):
            item = CartItem()
            item.index = index
            item.count = int(input.get_attribute("value"))
            item.price = round(float(span.text.replace("zł", "").replace(",", ".")) / item.count, 2)
            item.name = anchor.text
            result.append(item)
            index += 1
        return result

    def item_count(self, item_name=None):
        if not item_name:
            return sum(item.count for item in self.items())
        return sum(item.count for item in self.items() if item.name == item_name)

    def compute_total_price(self):
        return sum(item.compute_total_price() for item in self.items())

    def add_to_cart(self, item_id, item_count=1):
        item_page = ItemPage(self.driver, self.user_name, self.password, item_id)
        item_page.navigate()
        item_page.quantity_text_box().clear()
        item_page.quantity_text_box().send_keys(str(item_count))
        item_page.add_to_cart_button().click()
        item_page.wait_until_page_loaded()

    def go_to_checkout_page(self) -> CheckoutPage:
        self.go_to_checkout_button().click()
        self.wait_until_page_loaded()
        checkout_page = CheckoutPage(self.driver, self.user_name, self.password)
        return checkout_page

    def clear_cart(self):
        self.header_remove_button().click()
        self.remove_all_button().click()
        self.remove_all_confirm_button().click()
        self.wait_until_page_loaded()  # here must wait asn otherwise will fail

    def header_remove_button(self):
        return self.find_and_wait_for_clickable("button[data-role='header-remove-button']")

    def remove_all_button(self):
        return self.find_and_wait_for_clickable("button[data-role='remove-all-button']")

    def remove_all_confirm_button(self):
        return self.find_and_wait_for_clickable("delete-offers-confirm div button:nth-child(2)")

    def go_to_checkout_button(self):
        return self.find("button._13q9y._8tsq7._7qjq4")

    def continue_shopping_button(self):
        return self.find("a[data-analytics-click-label='continueShopping']")

    def _on_before_navigate(self):
        if self.login_before:
            self.login()

    def _on_just_navigate(self):
        self.driver.get("https://allegro.pl.allegrosandbox.pl/koszyk")

    def _on_after_navigate(self):
        if self.should_clear_cart and self.item_count() > 0:
            self.clear_cart()
