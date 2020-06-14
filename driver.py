from selenium import webdriver


class Driver:
    @staticmethod
    def create() -> webdriver.Chrome:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)  # jesli nie ma elementu, bedzie czekal do 10 sek.
        return driver
