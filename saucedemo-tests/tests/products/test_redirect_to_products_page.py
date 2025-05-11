import pytest
import logging
from selenium.webdriver.common.by import By

def test_redirect_to_products_page(driver, config):
    logging.info("----- Starting Test P1: Redirect after login -----")
    
    # Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(config["username"])
    driver.find_element(By.ID, "password").send_keys(config["password"])
    driver.find_element(By.ID, "login-button").click()
    
    # Assert URL
    expected_url = "https://www.saucedemo.com/inventory.html"
    assert driver.current_url == expected_url, f"Expected URL: {expected_url}, Found: {driver.current_url}"
    logging.info("Successfully redirected to the products page.")
