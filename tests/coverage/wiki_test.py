from base_test import BaseTest
from pages.wiki_page import WikiPage

class WikiTest(BaseTest):
    def test_wiki_button(self):
        page = WikiPage(self.driver)
        page.click_wiki_button()
        assert 'wiki' in self.driver.current_url

    def test_gear_hover(self):
        page = WikiPage(self.driver)
        page.hover(*WikiPage.WIKI_BUTTON)

    def test_weapons_option(self):
        page = WikiPage(self.driver)
        page.click_weapons_option()
        assert 'Weapons' in self.driver.current_url

    def test_table_item(self):
        page = WikiPage(self.driver)
        cartridge = page.check_cartridge()
        assert '5.45х39' in cartridge


