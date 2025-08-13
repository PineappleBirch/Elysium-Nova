from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

BASE_URL = "https://demo.applitools.com/"
LOGIN_FORM_SELECTOR = (By.CSS_SELECTOR, "form")
MAIN_APP_SELECTOR = (By.CSS_SELECTOR, ".element-wrapper")

def create_chrome_driver_with_options():
    chrome_options = Options()
    # Adding headless and standard resolution arguments
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--force-device-scale-factor=1")
    return webdriver.Chrome(options=chrome_options)

def capture_baseline_screenshots():
    print("Starting baseline image capture...")
    driver = create_chrome_driver_with_options()
    driver.set_window_size(1920, 1080)
    try:
        # Capture Login Page
        driver.get(BASE_URL)
        time.sleep(2)
        driver.find_element(*LOGIN_FORM_SELECTOR).screenshot("baseline/login_page_baseline.png")
        print(" -> Saved to baseline/login_page_baseline.png")

        # Log in and Capture Main App Page
        driver.find_element(By.ID, "username").send_keys("test")
        driver.find_element(By.ID, "password").send_keys("test")
        driver.find_element(By.ID, "log-in").click()
        time.sleep(2)
        driver.find_element(*MAIN_APP_SELECTOR).screenshot("baseline/main_app_page_baseline.png")
        print(" -> Saved to baseline/main_app_page_baseline.png")
    finally:
        driver.quit()
        print("Baseline capture complete.")

if __name__ == "__main__":
    capture_baseline_screenshots()