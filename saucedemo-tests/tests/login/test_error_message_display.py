import pytest
import logging
from selenium.webdriver.common.by import By

def test_error_message_display(driver):
    logging.info("----- Starting Test L8: Verify error messages are displayed correctly -----")

    try:
        # Step 1: Input wrong credentials
        driver.find_element(By.ID, "user-name").send_keys("wrong_user")
        driver.find_element(By.ID, "password").send_keys("wrong_pass")
        driver.find_element(By.ID, "login-button").click()

        # Step 2: Validate error message content
        error_container = driver.find_element(By.CLASS_NAME, "error-message-container")
        assert error_container.is_displayed(), "Error message is not displayed"

        error_text = error_container.text.strip()
        expected_text = "Epic sadface: Username and password do not match any user in this service"
        assert error_text == expected_text, f"Unexpected error message: {error_text}"
        logging.info("Correct error message displayed")

    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        pytest.fail(str(e))

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        pytest.fail(str(e))

    finally:
        logging.info("----- End of Test L8 -----")
