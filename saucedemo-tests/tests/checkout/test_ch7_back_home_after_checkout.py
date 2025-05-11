import pytest
import logging
from selenium.webdriver.common.by import By

def test_ch7_back_home_after_checkout(driver):
    logging.info("=== Starting Test CH7: Back Home after checkout ===")

    try:
        # Repeat steps to reach checkout complete
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
        driver.find_element(By.ID, "finish").click()

        # Click Back Home
        driver.find_element(By.ID, "back-to-products").click()
        assert "inventory" in driver.current_url
        logging.info("Successfully returned to product page.")

    except Exception as e:
        logging.error(f"Test failed: {e}")
        pytest.fail(str(e))

    logging.info("=== End of Test CH7 ===")
