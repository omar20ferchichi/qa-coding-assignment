import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_u3_tab_order(driver):
    logging.info("=== Starting Test U3: Accessibility - Tab order and focus behavior ===")

    try:
        driver.get("https://www.saucedemo.com/")
        body = driver.find_element(By.TAG_NAME, "body")

        body.send_keys(Keys.TAB)
        active = driver.switch_to.active_element
        assert active.get_attribute("id") == "user-name"
        logging.info("Focus is on username field")

        active.send_keys(Keys.TAB)
        active = driver.switch_to.active_element
        assert active.get_attribute("id") == "password"
        logging.info("Focus is on password field")

        active.send_keys(Keys.TAB)
        active = driver.switch_to.active_element
        assert active.get_attribute("id") == "login-button"
        logging.info("Focus is on login button")

    except Exception as e:
        logging.error(f"Test U3 failed: {e}")
        pytest.fail(str(e))

    logging.info("=== End of Test U3 ===")
