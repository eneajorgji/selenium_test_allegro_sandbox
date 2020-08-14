import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from driver import IMPLICIT_WAIT_TIME


class HomePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def navigate(self):
        self._on_before_navigate()
        self._on_just_navigate()
        self._on_after_navigate()

    def accept_policy(self):
        try:
            button = self.find("button[data-role='accept-consent']")
            button.click()
        except NoSuchElementException:
            pass

    def is_user_not_found(self):
        return "Nie znaleźliśmy użytkownika" in self._page_text()

    def find(self, path):
        return self.driver.find_element_by_css_selector(path)

    def find_many(self, path):
        return self.driver.find_elements_by_css_selector(path)

    def find_and_wait_for_clickable(self, path):
        return self._find_and_wait(path, expected_conditions.element_to_be_clickable)

    def find_and_wait_for_presence(self, path):
        return self._find_and_wait(path, expected_conditions.presence_of_element_located)

    def wait_until_page_loaded(self):
        time.sleep(IMPLICIT_WAIT_TIME)

    def _get_element_if_exists(self, path):
        element = self.driver.find_elements_by_css_selector(path)
        if len(element) > 0:
            return element[0]
        return None

    def _element_exists(self, path):
        return len(self.driver.find_elements_by_css_selector(path)) > 0

    def _find_and_wait(self, path, conditions):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(conditions((By.CSS_SELECTOR, path)))

    def _page_text(self):
        body = self.driver.find_element_by_tag_name("body")
        return body.text

    def _on_before_navigate(self):
        pass

    def _on_just_navigate(self):
        self.driver.get("https://allegro.pl.allegrosandbox.pl")

    def _on_after_navigate(self):
        self.accept_policy()
