from selenium.webdriver.common.by import By

class InventoryPage:
    """
    Page Object for the Sauce Demo inventory page.
    """

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver

    def is_on_inventory_page(self):
        """
        Verifies if the user is on the inventory page by checking for the title.
        """
        return self.driver.find_element(*self.PAGE_TITLE).is_displayed()