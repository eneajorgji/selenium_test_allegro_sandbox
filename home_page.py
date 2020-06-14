class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get("https://allegro.pl.allegrosandbox.pl")