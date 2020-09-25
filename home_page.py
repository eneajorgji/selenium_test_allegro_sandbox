import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from driver import Driver
from configuration import IMPLICIT_WAIT_TIME, MICRO_WAIT_TIME, ELEMENT_NOT_FOUND_EXCEPTION


class HomePage:
    def __init__(self, driver: Driver):
        self.driver = driver
        self.driver.put_to_session("policy_accepted", False)

    def navigate(self):
        self._on_before_navigate()
        self._on_just_navigate()
        self._on_after_navigate()

    def accept_policy(self):
        try:
            if not self.driver.get_from_session("policy_accepted"):
                button = self.find("button[data-role='accept-consent']")
                button.click()
                self.driver.update_in_session("policy_accepted", True)
        except ELEMENT_NOT_FOUND_EXCEPTION:
            pass

    def is_user_not_found(self):
        return "Nie znaleźliśmy użytkownika" in self._page_text()

    def find(self, path):
        try:
            return self.find_and_wait_for_clickable(path)
        except ELEMENT_NOT_FOUND_EXCEPTION:
            return self.driver.find_element_by_css_selector(path)

    def find_many(self, path):
        try:
            self.find_and_wait_for_clickable(path)
            return self.driver.find_elements_by_css_selector(path)
        except ELEMENT_NOT_FOUND_EXCEPTION:
            return []

    def find_and_wait_for_clickable(self, path):
        return self._find_and_wait(path, expected_conditions.element_to_be_clickable)

    def find_and_wait_for_presence(self, path):
        return self._find_and_wait(path, expected_conditions.presence_of_element_located)

    def is_loaded(self):
        state = self.driver.execute_script("return document.readyState")
        return state == "complete"

    def wait_until_page_loaded(self):
        while True:
            if self.is_loaded():
                break
            time.sleep(MICRO_WAIT_TIME)

    def wait_until_page_url_contains(self, what):
        while True:
            if what not in self.driver.current_url:
                break
            time.sleep(MICRO_WAIT_TIME)

    def wait_a_moment(self, moment=IMPLICIT_WAIT_TIME):
        time.sleep(moment)

    def send_keys_to_activate_element(self, keys):
        self.driver.switch_to.active_element.send_keys(keys)

    def _get_element_if_exists(self, path):
        element = self.driver.find_elements_by_css_selector(path)
        if len(element) > 0:
            return element[0]
        return None

    def _element_exists(self, path):
        return len(self.driver.find_elements_by_css_selector(path)) > 0

    def _find_and_wait(self, path, conditions):
        wait = WebDriverWait(self.driver, IMPLICIT_WAIT_TIME)
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
