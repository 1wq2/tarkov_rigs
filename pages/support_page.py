from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SupportPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    SUPPORT_BUTTON = (By.XPATH, "//a[contains(text(),'Support')]")
    SUPPORT_SEARCH = (By.XPATH, "//input[@id='main_search']")
    ERROR_208 = (By.XPATH, "//ul[@id='knowledge_results']//a[contains(text(),'Error 208')]")
    ERROR_INFO = (By.XPATH, "//*[@itemprop='name headline' and contains(text(),'Error 208')]")

