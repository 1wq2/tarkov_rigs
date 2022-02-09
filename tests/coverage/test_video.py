import time
from tests.coverage.test_base import TestBase
from pages.video_page import VideoPage


class TestVideo(TestBase):
    def test_video_link(self):
        page = VideoPage(self.driver)
        page.hover(*VideoPage.VIDEO_BANNER)
        page.click(*VideoPage.VIDEO_BANNER)

    def test_iframe(self):
        page = VideoPage(self.driver)
        iframe = self.driver.find_element(*VideoPage.IFRAME)
        self.driver.switch_to.frame(iframe)
        page.wait_element(*VideoPage.YTB_PLAY_BUTTON)
        page.click(*VideoPage.YTB_PLAY_BUTTON)

    def test_video_playback(self):
        page = VideoPage(self.driver)
        time.sleep(5)
        page.hover(*VideoPage.CURRENT_TIME)
        current_time = self.driver.find_element(*VideoPage.CURRENT_TIME).text
        print("LOOK AT THIS CURRENT TIME ")
        print(current_time)
        assert current_time != ''

