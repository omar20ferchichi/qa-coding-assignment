import pytest
import logging
from selenium.webdriver.common.by import By

def test_navigate_to_cart_and_verify_items(driver, config):
    logging.info("----- Starting Test C4: Verify Items in Cart Page -----")

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(config['username'])
    driver.find_element(By.ID, "password").send_keys(config['password'])
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 1, f"Expected 1 item in cart, found {len(cart_items)}"
    logging.info("Verified item is present in the cart page.")
