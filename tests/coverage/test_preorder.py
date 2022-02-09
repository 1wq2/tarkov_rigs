from tests.coverage.test_base import TestBase
from pages.preorder_page import PreorderPage


class TestPreorder(TestBase):
    def test_preorder_button(self):
        page = PreorderPage(self.driver)
        page.click(*PreorderPage.PREORDER_BUTTON)

    def test_preorder_option(self):
        page = PreorderPage(self.driver)
        page.wait_element(*PreorderPage.PREORDER_ITEM)
        page.click(*PreorderPage.PREORDER_ITEM)

    def test_reg_modal(self):
        page = PreorderPage(self.driver)
        page.wait_element(*PreorderPage.REG_MODAL)
        info = self.driver.find_element(*PreorderPage.REG_MODAL).text
        print(info)
        assert 'NEED TO REGISTER' in info

