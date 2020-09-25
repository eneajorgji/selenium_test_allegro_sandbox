from selenium import webdriver
from configuration import IMPLICIT_WAIT_TIME


class Driver(webdriver.Chrome):
    def __init__(self, options):
        webdriver.Chrome.__init__(self, options=options)
        self.session = {}

    @staticmethod
    def create():
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = Driver(options)
        driver.implicitly_wait(IMPLICIT_WAIT_TIME)
        return driver

    def put_to_session(self, name, value):
        if name not in self.session:
            self.session[name] = value

    def update_in_session(self, name, value):
        self.session[name] = value

    def get_from_session(self, name):
        return self.session[name]
