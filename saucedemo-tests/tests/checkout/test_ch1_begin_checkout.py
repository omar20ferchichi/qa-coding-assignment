import pytest
import logging
from selenium.webdriver.common.by import By

def test_ch1_begin_checkout(driver):
    logging.info("=== Starting Test CH1: Begin checkout from cart ===")

    try:
        # Login first
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        logging.info("Logged in successfully.")

        # Add item to cart
        driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        logging.info("Added item to cart.")

        # Go to cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        logging.info("Navigated to cart page.")

        # Click checkout
        driver.find_element(By.ID, "checkout").click()
        assert "checkout-step-one" in driver.current_url
        logging.info("Navigated to checkout step one.")

    except Exception as e:
        logging.error(f"Test failed: {e}")
        pytest.fail(str(e))

    logging.info("=== End of Test CH1 ===")
