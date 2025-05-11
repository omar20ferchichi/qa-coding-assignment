import pytest
import logging
from selenium.webdriver.common.by import By

def test_return_to_products_from_cart(driver, config):
    logging.info("----- Starting Test C7: Return to Products Page from Cart -----")

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(config['username'])
    driver.find_element(By.ID, "password").send_keys(config['password'])
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    driver.find_element(By.ID, "continue-shopping").click()
    assert "inventory" in driver.current_url, "Should return to product list after continue shopping"
    logging.info("Returned to products page successfully after clicking 'Continue Shopping'.")
