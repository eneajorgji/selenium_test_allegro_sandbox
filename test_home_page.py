from unittest import TestCase
from driver import Driver
from home_page import HomePage


class TestHomePage(TestCase):

    def setUp(self):
        self.driver = Driver.create()
        self.page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_navigate(self):
        self.page.navigate()
        assert "Allegro" in self.driver.title
