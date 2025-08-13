import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    # Adding headless and standard resolution arguments
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--force-device-scale-factor=1")

    driver_instance = webdriver.Chrome(options=chrome_options)
    driver_instance.set_window_size(1920, 1080)
    yield driver_instance
    driver_instance.quit()