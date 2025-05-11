import pytest
import logging
from selenium.webdriver.common.by import By

def test_e2_locked_out_user_cannot_add_items(driver):
    logging.info("=== Starting Test E2: locked_out_user add to cart attempt ===")
    try:
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Expect login to fail
        error = driver.find_element(By.CLASS_NAME, "error-message-container")
        assert error.is_displayed()
        logging.info("Login blocked as expected for locked_out_user.")

    except Exception as e:
        logging.error(f"Test E2 failed: {e}")
        pytest.fail(str(e))
    logging.info("=== End of Test E2 ===")
