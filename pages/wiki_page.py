from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class WikiPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    WIKI_BUTTON = (By.XPATH, "//a[contains(text(),'Wiki')]")
    GEAR_HOVER = (By.XPATH, "//div[@class='main-container']//a[contains(@href,'Weapons')]//ancestor::li[@class='wds-dropdown ']")
    WEAPONS_LABEL = (By.XPATH,
                     "//div[@class='main-container']//div[contains(@class,'wds-dropdown__content')]//a[contains(@href,'/wiki/Weapons')]")
    CARTRIDGE = (By.XPATH, "//table[contains(@class,'wikitable')]//a[@title='AK-74M']//ancestor::tr//a[contains(@title,'mm')]")

    def click_wiki_button(self):
        wiki_button = self.driver.find_element(*WikiPage.WIKI_BUTTON)
        wiki_button.click()

    def click_weapons_option(self):
        weapons_label = self.driver.find_element(*WikiPage.WEAPONS_LABEL)
        weapons_label.click()

