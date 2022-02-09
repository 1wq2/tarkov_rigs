from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class VideoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    VIDEO_BANNER = (By.XPATH, "//section[@id='banner_39_youtube']")
    IFRAME = (By.XPATH, "//iframe[@id='VideoPlayer_39']")
    YTB_PLAY_BUTTON = (By.XPATH, "//button[@aria-label='Play'][1]")
    CURRENT_TIME = (By.XPATH, "//*[@class='ytp-time-current'][normalize-space(text())]")
