from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch
from selenium.webdriver.common.by import By
import time
import pytest

# --- Configuration ---
LOGIN_FORM_SELECTOR = (By.CSS_SELECTOR, "form")
MAIN_APP_SELECTOR = (By.CSS_SELECTOR, ".element-wrapper")
LOGIN_BUTTON_SELECTOR = (By.ID, "log-in")
PASSWORD_FIELD_LOCATOR = (By.ID, "password")
BALANCES_LOCATOR = (By.CSS_SELECTOR, "div.element-balances")



# --- Comparison Thresholds ---
PIXEL_THRESHOLD = 0.2
FAILURE_THRESHOLD_PERCENT = 0.01

def compare_images(baseline_path, actual_path, diff_path):
    """
    Compares two images with tolerance for minor anti-aliasing differences.
    """
    img_baseline = Image.open(baseline_path)
    img_actual = Image.open(actual_path)
    if img_baseline.size != img_actual.size:
        print(f"Warning: Image sizes differed. Resizing actual image to match baseline.")
        img_actual = img_actual.resize(img_baseline.size)
    img_diff = Image.new("RGBA", img_baseline.size)
    mismatched_pixels = pixelmatch(img_baseline, img_actual, img_diff, threshold=PIXEL_THRESHOLD)
    total_pixels = img_baseline.size[0] * img_baseline.size[1]
    mismatch_percentage = mismatched_pixels / total_pixels
    if mismatch_percentage > 0:
        img_diff.save(diff_path)
    return mismatch_percentage

def test_login_page_visuals(driver):
    """
    Verifies the visual appearance of the login page.
    """
    driver.get("https://demo.applitools.com/")
    time.sleep(2)
    actual_path = "actual/login_page_actual.png"
    driver.find_element(*LOGIN_FORM_SELECTOR).screenshot(actual_path)
    mismatch = compare_images("baseline/login_page_baseline.png", actual_path, "diff/login_page_diff.png")
    assert mismatch <= FAILURE_THRESHOLD_PERCENT

def test_main_app_page_visuals(driver):
    """
    Verifies the visual appearance of the main app page after logging in.
    """
    driver.get("https://demo.applitools.com/")
    driver.find_element(By.ID, "username").send_keys("test")
    driver.find_element(By.ID, "password").send_keys("test")
    driver.find_element(By.ID, "log-in").click()
    time.sleep(2)
    actual_path = "actual/main_app_page_actual.png"
    driver.find_element(*MAIN_APP_SELECTOR).screenshot(actual_path)
    mismatch = compare_images("baseline/main_app_page_baseline.png", actual_path, "diff/main_app_page_diff.png")
    assert mismatch <= FAILURE_THRESHOLD_PERCENT

def test_detects_bug_on_login_page1(driver):
    """
    Deliberately alters the page and verifies a visual difference is detected.
    """
    driver.get("https://demo.applitools.com/")
    time.sleep(2)
    login_button = driver.find_element(*LOGIN_BUTTON_SELECTOR)
    driver.execute_script("arguments[0].style.backgroundColor = 'red';", login_button)
    time.sleep(1)
    actual_path = "actual/login_page_bug_1.png"
    driver.find_element(*LOGIN_FORM_SELECTOR).screenshot(actual_path)
    mismatch = compare_images("baseline/login_page_baseline.png", actual_path, "diff/login_page_diff_1.png")
    assert mismatch > FAILURE_THRESHOLD_PERCENT

def test_detects_bug_on_login_page2(driver):
    """
    Deliberately alters the page by hiding the Facebook icon and verifies a visual difference is detected.
    """
    driver.get("https://demo.applitools.com/")
    time.sleep(2)

    password_field = driver.find_element(*PASSWORD_FIELD_LOCATOR)
    driver.execute_script("arguments[0].style.display = 'none';", password_field)

    time.sleep(1)
    actual_path = "actual/login_page_bug_2.png"
    driver.find_element(*LOGIN_FORM_SELECTOR).screenshot(actual_path)
    mismatch = compare_images("baseline/login_page_baseline.png", actual_path, "diff/login_page_diff_2.png")
    assert mismatch > FAILURE_THRESHOLD_PERCENT


def test_detects_bug_on_main_app_page(driver):
    """
    Verifies that a visual difference is detected on the main app page
    after hiding the logged user info element.
    """
    driver.get("https://demo.applitools.com/")
    driver.find_element(By.ID, "username").send_keys("test")
    driver.find_element(By.ID, "password").send_keys("test")
    driver.find_element(By.ID, "log-in").click()
    time.sleep(2)

    logged_user_elem = driver.find_element(*BALANCES_LOCATOR)
    driver.execute_script("arguments[0].style.display = 'none';", logged_user_elem)

    time.sleep(1)
    actual_path = "actual/main_app_page_bug.png"
    driver.find_element(*MAIN_APP_SELECTOR).screenshot(actual_path)
    mismatch = compare_images("baseline/main_app_page_baseline.png", actual_path, "diff/main_app_page_diff.png")
    assert mismatch > FAILURE_THRESHOLD_PERCENT
