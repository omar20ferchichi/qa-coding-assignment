import pytest
import logging
from selenium.webdriver.common.by import By

def test_e1_checkout_with_empty_cart(driver):
    logging.info("=== Starting Test E1: Checkout with empty cart ===")
    try:
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        logging.info("Logged in successfully.")

        # Go directly to cart without adding items
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        logging.info("Clicked checkout with empty cart.")

        # Still allows proceeding - validate user lands on checkout page
        assert "checkout-step-one" in driver.current_url
        logging.warning("Checkout page opened with empty cart (expected behavior).")

    except Exception as e:
        logging.error(f"Test E1 failed: {e}")
        pytest.fail(str(e))
    logging.info("=== End of Test E1 ===")
