from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BookPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    MERCH_BUTTON = (By.XPATH, "//a[contains(text(),'Merch')]")
    BOOK_BUTTON = (By.XPATH, "//p[contains(text(),'Книги')]")
    BOOK_ITEM = (By.XPATH, "//span[contains(text(),'Книга \"Хозяин Ночи\" Цифровое издание (Русская версия)')]//ancestor::div[@class='tarkov-card-text mt-0']/span")