from search_page import SearchPage
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from home_page import HomePage
from selenium.webdriver.support import expected_conditions


class SearchManyPage(SearchPage):
    def __init__(self, driver: webdriver.Chrome):
        # super(driver)  # wywoluje instruktora klasy HomePage
        SearchPage.__init__(self, driver)

    # waits for the element to be visible - RECHECK
    def find_and_wait_for_visible(self, path):
        return self._find_and_wait(path, expected_conditions.visibility_of_element_located)

    # waits for the element to be clickable - RECHECK
    def find_and_wait_for_clickable(self, path):
        return self._find_and_wait(path, expected_conditions.element_to_be_clickable)

    def search_combo_box(self):
        return Select(self.find("select._d25db_ZZIhH._1h7wt._k70df.m7er_k4.m7er_wn"))

    def search_button(self):
        return self.find("button._d25db_10Nyi._13q9y._8tsq7._1q2ua")

    def search_many_link(self):
        return self.find("button._w7z6o._ypulx.mp4t_0.m3h2_0.mryx_0.munh_0.mwl7_0")

    def search_many_input(self, index):
        return self.find(f"#input{index}")

    def search_many_additional_button(self):
        return self.find("button[data-role='add-next-input-btn']")

    def search_many_button(self):
        return self.find("button._13q9y._8tsq7.m7er_k4.m7er_k4.m7er_wn")

    def search_many_remove_button(self):
        pass

    def has_multi_offers(self):
        try:
            self.find_and_wait_for_clickable("button._7qjq4.b1l04.bp58a")
            return True
        except:
            return False
