from selenium import webdriver


class Driver:
    @staticmethod
    def create() -> webdriver.Chrome:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=options)
        driver.implicitly_wait(10)
        return driver
