from tests.coverage.test_base import BaseTest
from pages.wiki_page import WikiPage


class TestWiki(BaseTest):
    def test_wiki_button(self):
        page = WikiPage(self.driver)
        page.click_wiki_button()
        page.wait_page(self.driver)

    def test_gear_hover(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        page = WikiPage(self.driver)
        page.hover(*WikiPage.GEAR_HOVER)
        page.click(*WikiPage.WEAPONS_LABEL)

    def test_table_item(self):
        cartridge = self.driver.find_element(*WikiPage.CARTRIDGE).get_attribute('title')
        print(cartridge)
        assert '5.45' in cartridge


