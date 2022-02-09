from tests.coverage.test_base import TestBase
from pages.book_page import BookPage


class TestBook(TestBase):
    def test_merch_button(self):
        page = BookPage(self.driver)
        page.click(*BookPage.MERCH_BUTTON)
        page.wait_page(self.driver)

    def test_book_option(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        page = BookPage(self.driver)
        page.wait_element(*BookPage.BOOK_BUTTON)
        page.click(*BookPage.BOOK_BUTTON)

    def test_book_price(self):
        page = BookPage(self.driver)
        page.wait_element(*BookPage.BOOK_ITEM)
        price = self.driver.find_element(*BookPage.BOOK_ITEM).text
        print(price)
        assert '260' in price

