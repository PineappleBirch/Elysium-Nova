import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Define the login URL once to avoid repetition
LOGIN_URL = "https://www.saucedemo.com/"

def test_successful_login(driver):
    """
    Verifies successful login using standard user credentials.
    """
    driver.get(LOGIN_URL)
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)
    assert inventory_page.is_on_inventory_page()

def test_locked_out_user(driver):
    """
    Verifies that a locked-out user cannot log in.
    """
    driver.get(LOGIN_URL)
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")
    assert login_page.get_error_message() == "Epic sadface: Sorry, this user has been locked out."

def test_incorrect_password(driver):
    """
    Verifies login fails with a valid username and incorrect password.
    """
    driver.get(LOGIN_URL)
    login_page = LoginPage(driver)
    login_page.login("standard_user", "wrong_password")
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"

def test_invalid_username(driver):
    """
    Verifies login fails with an invalid username.
    """
    driver.get(LOGIN_URL)
    login_page = LoginPage(driver)
    login_page.login("invalid_user", "secret_sauce")
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"

def test_empty_username(driver):
    """
    Verifies login fails with an empty username.
    """
    driver.get(LOGIN_URL)
    login_page = LoginPage(driver)
    login_page.login("", "secret_sauce")
    assert login_page.get_error_message() == "Epic sadface: Username is required"

def test_empty_password(driver):
    """
    Verifies login fails with an empty password.
    """
    driver.get(LOGIN_URL)
    login_page = LoginPage(driver)
    login_page.login("standard_user", "")
    assert login_page.get_error_message() == "Epic sadface: Password is required"

def test_empty_credentials(driver):
    """
    Verifies login fails with empty credentials.
    """
    driver.get(LOGIN_URL)
    login_page = LoginPage(driver)
    login_page.login("", "")
    assert login_page.get_error_message() == "Epic sadface: Username is required"