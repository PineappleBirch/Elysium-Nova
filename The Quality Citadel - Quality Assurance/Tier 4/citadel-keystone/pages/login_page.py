from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """
    Page Object for the Sauce Demo login page.
    """

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE_CONTAINER = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        # Defining an explicit wait of 10 seconds
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        """
        Waits for the username field to be visible and enters the username.
        """
        username_field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        username_field.send_keys(username)

    def enter_password(self, password):
        """
        Waits for the password field to be visible and enters the password.
        """
        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        password_field.send_keys(password)

    def click_login(self):
        """
        Waits for the login button to be clickable and clicks it.
        """
        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()

    def login(self, username, password):
        """
        Performs a full login action with waits.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """
        Waits for the error message to be visible and returns its text.
        """
        error_message = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE_CONTAINER))
        return error_message.text