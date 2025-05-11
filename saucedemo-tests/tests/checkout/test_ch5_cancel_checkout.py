import pytest
import logging
from selenium.webdriver.common.by import By

def test_ch5_cancel_checkout(driver):
    logging.info("=== Starting Test CH5: Cancel checkout ===")

    try:
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Doe")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        # Cancel checkout
        driver.find_element(By.ID, "cancel").click()
        assert "inventory" in driver.current_url
        logging.info("Successfully cancelled checkout.")

    except Exception as e:
        logging.error(f"Test failed: {e}")
        pytest.fail(str(e))

    logging.info("=== End of Test CH5 ===")
