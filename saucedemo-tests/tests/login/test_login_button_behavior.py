import pytest
import logging
from selenium.webdriver.common.by import By

def test_login_button_behavior(driver):
    logging.info("----- Starting Test L10: Verify login button behavior for empty fields -----")

    try:
        login_button = driver.find_element(By.ID, "login-button")

        # On this site, the button is not technically disabled, so check if it does nothing or error
        login_button.click()

        error_container = driver.find_element(By.CLASS_NAME, "error-message-container")
        assert error_container.is_displayed(), "Error not shown on clicking login with empty fields"
        logging.info("Login button is not disabled but triggers an appropriate error message")

    except Exception as e:
        logging.error(f"Test L10 failed: {e}")
        pytest.fail(str(e))

    finally:
        logging.info("----- End of Test L10 -----")
