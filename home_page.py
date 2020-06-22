from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def navigate(self):
        self.driver.get("https://allegro.pl.allegrosandbox.pl")
        self.accept_button().click()

    def accept_button(self):
        return self.find("button._13q9y._8hkto.munh_56_m.m7er_k4.m7er_wn.m7er_56_m")

    def is_user_not_found(self):
        return self._element_exists("div.opbox-sheet._26e29_11PCu.card._9f0v0.msts_n7")

    def find(self, path):
        return self.driver.find_element_by_css_selector(path)

    def find_and_wait_for_visible(self, path):
        return self._find_and_wait(path, expected_conditions.visibility_of_element_located)

    def find_and_wait_for_clickable(self, path):
        return self._find_and_wait(path, expected_conditions.element_to_be_clickable)

    def _get_element_if_exists(self, path):
        element = self.driver.find_elements_by_css_selector(path)
        if len(element) > 0:
            return element[0]
        return None

    def _element_exists(self, path):
        return len(self.driver.find_elements_by_css_selector(path)) > 0

    def _find_and_wait(self, path, conditions):  # this is helping function
        wait = WebDriverWait(self.driver, 10)
        return wait.until(conditions((By.CSS_SELECTOR, path)))
