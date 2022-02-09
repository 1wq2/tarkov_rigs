from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SortingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    RATING_BUTTON = (By.XPATH, "//a[contains(text(),'Ratings')]")
    RATING_DROPDOWN = (By.XPATH, "//div[@class='category switcher inlinetop']")
    PLAYTIME_OPTION = (By.XPATH, "//li[@data-val='timeOnline']")
    RECORDS = (By.XPATH, "//div[contains(@class, 'table')]//tr")
    LEVEL_DATA = (By.XPATH, "//div[contains(@class, 'table')]//td[@data-col-name= 'Lvl']")

