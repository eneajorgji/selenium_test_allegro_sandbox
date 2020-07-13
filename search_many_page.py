from search_page import SearchPage
from selenium import webdriver


class SearchManyPage(SearchPage):
    def __init__(self, driver: webdriver.Chrome):
        SearchPage.__init__(self, driver)

    def search_many_link(self):
        return self.find("button._w7z6o._ypulx.mp4t_0.m3h2_0.mryx_0.munh_0.mwl7_0")

    def search_many_input(self, index):
        return self.find_and_wait_for_clickable(f"#input{index}")

    def search_many_additional_button(self):
        return self.find("button[data-role='add-next-input-btn']")

    def search_many_button(self):
        return self.find("button._13q9y._8tsq7.m7er_k4.m7er_k4.m7er_wn")

    def search_many_remove_button(self, index):
        return self.find_and_wait_for_clickable(f"button[data-role='remove-btn-{index}']")

    def has_offers(self):  # polimorphism
        try:
            self.find_and_wait_for_clickable("button._7qjq4.b1l04.bp58a")
            return True
        except:
            return False
