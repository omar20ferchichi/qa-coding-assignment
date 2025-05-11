import pytest
import logging
from selenium.webdriver.common.by import By

def test_login_empty_username_password(driver):
    logging.info("----- Starting Test L7: Login with empty username and/or password -----")

    try:
        # Step 1: Locate username and password fields
        username_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")

        # Step 2: Leave fields empty and click login
        logging.info("Step 2: Leaving username and password fields empty")
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Step 3: Verify error message appears
        logging.info("Step 3: Verifying error message is displayed")
        error_msg = driver.find_element(By.CLASS_NAME, "error-message-container")
        assert error_msg.is_displayed(), "Error message not displayed for empty fields"
        logging.info("Error message displayed as expected")

    except Exception as e:
        logging.error(f"Test L7 failed: {e}")
        pytest.fail(str(e))

    finally:
        logging.info("----- End of Test L7 -----")
