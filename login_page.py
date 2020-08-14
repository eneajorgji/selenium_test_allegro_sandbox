from selenium import webdriver
from home_page import HomePage


class LoginPage(HomePage):
    def __init__(self, driver: webdriver.Chrome, user_name, password):
        HomePage.__init__(self, driver)
        self.user_name = user_name
        self.password = password

    def login(self):
        self.driver.get("https://allegro.pl.allegrosandbox.pl/login/form")
        self.accept_policy()
        self.user_name_text_box().send_keys(self.user_name)
        self.password_text_box().send_keys(self.password)
        self.login_button().click()
        self.wait_until_page_loaded()

    def logout(self):
        self.driver.get("https://allegro.pl.allegrosandbox.pl/logout.php")
        self.accept_policy()
        self.wait_until_page_loaded()

    def is_logged_in(self):
        try:
            span = self.find_and_wait_for_presence("span[data-role='header-username']")
            return span.text == self.user_name
        except:
            return False

    def user_name_text_box(self):
        return self.find("#username")

    def password_text_box(self):
        return self.find("#password")

    def login_button(self):
        return self.find("#login-button")
