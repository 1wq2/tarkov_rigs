from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class PreorderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    PREORDER_BUTTON = (By.XPATH, "//img[@class='preorder_button']")
    PREORDER_ITEM = (By.XPATH, "//div[@class='button' and contains(text(),'Pre-order')][1]")
    REG_MODAL = (By.XPATH, "//div[@id='modal']//h4")