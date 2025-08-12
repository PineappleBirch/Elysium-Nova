import pytest
from core.webdriver_factory import WebDriverFactory

# To make the browser open only once for the entire test session, use scope="session".
# To make the browser open and close for every single test function, change to scope="function".
# "function" is more reliable for test isolation, while "session" is much faster.
@pytest.fixture(scope="session")
def driver(request):
    """
    Fixture to create and quit a WebDriver instance for the entire test session.
    """
    wdf = WebDriverFactory(browser="chrome")
    driver_instance = wdf.get_webdriver_instance()

    yield driver_instance

    # Teardown: This code runs after the entire test session is finished
    driver_instance.quit()