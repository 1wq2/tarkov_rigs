import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    # options.add_argument("--incognito")
    options.add_argument("--start-fullscreen")
    # options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://www.escapefromtarkov.com/")
    request.cls.driver = driver
    yield
    driver.quit()

