import pytest
import logging
from selenium.webdriver.common.by import By

def test_ch3_blank_fields_validation(driver):
    logging.info("=== Starting Test CH3: Blank fields validation ===")

    try:
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        # Leave fields blank
        driver.find_element(By.ID, "continue").click()
        error = driver.find_element(By.CLASS_NAME, "error-message-container")
        assert error.is_displayed()
        logging.info("Validation error displayed for blank fields.")

    except Exception as e:
        logging.error(f"Test failed: {e}")
        pytest.fail(str(e))

    logging.info("=== End of Test CH3 ===")
