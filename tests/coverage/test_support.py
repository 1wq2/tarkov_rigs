from tests.coverage.test_base import TestBase
from pages.support_page import SupportPage


class TestSupport(TestBase):
    def test_support_button(self):
        page = SupportPage(self.driver)
        page.click(*SupportPage.SUPPORT_BUTTON)

    def test_search_field(self):
        page = SupportPage(self.driver)
        self.driver.find_element(*SupportPage.SUPPORT_SEARCH).send_keys('Error 208')
        page.wait_element(*SupportPage.ERROR_208)
        page.click(*SupportPage.ERROR_208)

    def test_error_info(self):
        error_info = self.driver.find_element(*SupportPage.ERROR_INFO).text
        print(error_info)
        assert '208' in error_info
