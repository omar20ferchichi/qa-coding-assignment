import pytest
import logging
from selenium.webdriver.common.by import By

def test_add_multiple_items_to_cart(driver, config):
    logging.info("----- Starting Test C3: Add Multiple Products to Cart -----")

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(config['username'])
    driver.find_element(By.ID, "password").send_keys(config['password'])
    driver.find_element(By.ID, "login-button").click()

    items = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]

    for item_id in items:
        driver.find_element(By.ID, item_id).click()
        logging.info(f"Added item to cart: {item_id}")

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == str(len(items)), f"Expected {len(items)} items in cart, found {cart_badge.text}"
    logging.info("Cart badge correctly reflects number of items added.")
