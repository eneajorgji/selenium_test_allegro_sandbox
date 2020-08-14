from selenium import webdriver

IMPLICIT_WAIT_TIME = 3


class Driver:
    @staticmethod
    def create() -> webdriver.Chrome:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(IMPLICIT_WAIT_TIME)
        return driver
