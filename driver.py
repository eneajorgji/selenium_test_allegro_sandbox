from selenium import webdriver


class Driver:
    @staticmethod
    def create() -> webdriver.Chrome:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)  # will wait for 10 sec if there is no elements
        return driver
