import configparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):
        """
        Gets a WebDriver instance with a fresh, temporary user profile
        to ensure all pop-ups and browser UI are disabled.
        """
        config = configparser.ConfigParser()
        config.read('configs/config.ini')
        base_url = config.get('WEB', 'base_url')

        if self.browser == "chrome":
            chrome_options = Options()

            # Core arguments to create a clean, isolated session
            chrome_options.add_argument("--no-first-run")
            chrome_options.add_argument("--no-default-browser-check")
            chrome_options.add_argument("--disable-popup-blocking")

            # Arguments to disable disruptive UI features
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--disable-extensions")

            # Forcefully disable the password manager UI
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            }
            chrome_options.add_experimental_option("prefs", prefs)

            driver = webdriver.Chrome(options=chrome_options)
        else:
            driver = webdriver.Firefox()

        driver.maximize_window()
        driver.get(base_url)
        return driver