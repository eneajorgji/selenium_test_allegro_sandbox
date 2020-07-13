from unittest import TestCase

from driver import Driver
from login_page import LoginPage
from configuration import USER_NAME, PASSWORD


class TestLoginPage(TestCase):
    def setUp(self):
        self.driver = Driver.create()
        self.page = LoginPage(self.driver, USER_NAME, PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.page.navigate()
        self.page.login()

        assert self.page.is_logged_in()

    def test_logout(self):
        self.page.navigate()
        self.page.login()
        self.page.logout()

        assert not self.page.is_logged_in()
