import pytest
import logging
from selenium.webdriver.common.by import By

def test_six_products_displayed(driver, config):
    logging.info("----- Starting Test P2: 6 Products Displayed -----")
    
    # Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(config["username"])
    driver.find_element(By.ID, "password").send_keys(config["password"])
    driver.find_element(By.ID, "login-button").click()

    # Verify products
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) == 6, f"Expected 6 products, found {len(products)}"
    logging.info("6 products displayed correctly.")
