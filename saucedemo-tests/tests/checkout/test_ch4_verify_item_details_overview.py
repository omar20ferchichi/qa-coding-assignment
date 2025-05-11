import pytest
import logging
from selenium.webdriver.common.by import By

def test_ch4_verify_item_details_overview(driver):
    logging.info("=== Starting Test CH4: Verify item details on overview page ===")

    try:
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        # Fill checkout
        driver.find_element(By.ID, "first-name").send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Doe")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        # Check item details
        item = driver.find_element(By.CLASS_NAME, "inventory_item_name")
        assert item.is_displayed()
        logging.info("Item is visible on checkout overview page.")

    except Exception as e:
        logging.error(f"Test failed: {e}")
        pytest.fail(str(e))

    logging.info("=== End of Test CH4 ===")
