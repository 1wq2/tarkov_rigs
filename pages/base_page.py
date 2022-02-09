from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(locator))
        # ActionChains(self.driver).move_to_element(element).perform()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()

    def wait_page(self, driver):
        try:
            WebDriverWait(driver, 5).until(EC.url_changes)
        except TimeoutException:
            print("\n * PAGE FAILED TO LOAD!")
            self.driver.quit()

    def click(self, *locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        element.click()
