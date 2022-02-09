import time
from tests.coverage.test_base import TestBase
from pages.sorting_page import SortingPage


class TestSorting(TestBase):
    def test_rating_button(self):
        page = SortingPage(self.driver)
        page.click(*SortingPage.RATING_BUTTON)
        page.wait_page(self.driver)

    def test_rating_dropdown(self):
        page = SortingPage(self.driver)
        page.wait_element(*SortingPage.RATING_DROPDOWN)
        page.click(*SortingPage.RATING_DROPDOWN)
        page.wait_element(*SortingPage.PLAYTIME_OPTION)
        page.click(*SortingPage.PLAYTIME_OPTION)
        page.wait_page(self.driver)

    def test_record_data(self):
        page = SortingPage(self.driver)
        page.wait_elements(*SortingPage.RECORDS)
        records = self.driver.find_elements(*SortingPage.RECORDS)
        print(len(records))
        assert len(records) == 100
        level_data = self.driver.find_elements(*SortingPage.LEVEL_DATA)
        levels = [int(el.text) for el in level_data]
        print(levels)
        assert all(1 <= i <= 58 for i in levels) is True
