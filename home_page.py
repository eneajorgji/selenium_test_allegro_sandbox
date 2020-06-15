from selenium import webdriver


class HomePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def navigate(self):
        self.driver.get("https://allegro.pl.allegrosandbox.pl")

    def accept_button(self):
        return self.find("button._13q9y._8hkto.munh_56_m.m7er_k4.m7er_wn.m7er_56_m")

    def find(self, path):
        return self.driver.find_element_by_css_selector(path)
