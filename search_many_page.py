from search_page import SearchPage
from selenium import webdriver


class SearchManyPage(SearchPage):
    def __init__(self, driver: webdriver.Chrome):
        SearchPage.__init__(self, driver)

    def search_many_link(self):
        return self.find("button[data-role='multisearch-button']")

    def search_many_input(self, index):
        return self.find_and_wait_for_clickable(f"#input{index}")

    def search_many_additional_button(self):
        return self.find("button[data-role='add-next-input-btn']")

    def search_many_button(self):
        return self.find("div[data-role='modal'] button[type='submit']")

    def search_many_remove_button(self, index):
        return self.find_and_wait_for_clickable(f"button[data-role='remove-btn-{index}']")

    def has_offers(self):
        return "Nie ma sprzedawców" not in self._page_text()
