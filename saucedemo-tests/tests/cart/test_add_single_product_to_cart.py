import pytest
import logging
from selenium.webdriver.common.by import By

def test_add_single_product_to_cart(driver, config):
    logging.info("----- Starting Test C1: Add Product to Cart from Product List -----")

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(config['username'])
    driver.find_element(By.ID, "password").send_keys(config['password'])
    driver.find_element(By.ID, "login-button").click()

    add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_button.click()
    logging.info("Clicked 'Add to Cart' on Sauce Labs Backpack")

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "Cart badge should show 1 item"
    logging.info("Cart badge correctly shows 1 item.")
