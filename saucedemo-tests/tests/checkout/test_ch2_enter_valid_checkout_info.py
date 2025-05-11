import pytest
import logging
from selenium.webdriver.common.by import By

def test_ch2_enter_valid_checkout_info(driver):
    logging.info("=== Starting Test CH2: Valid checkout info ===")

    try:
        # Precondition: Log in, add item, go to checkout
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        # Enter valid info
        driver.find_element(By.ID, "first-name").send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Doe")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        logging.info("Entered checkout info.")

        # Continue
        driver.find_element(By.ID, "continue").click()
        assert "checkout-step-two" in driver.current_url
        logging.info("Moved to checkout overview.")

    except Exception as e:
        logging.error(f"Test failed: {e}")
        pytest.fail(str(e))

    logging.info("=== End of Test CH2 ===")
