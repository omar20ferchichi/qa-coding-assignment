import pytest
import logging
from selenium.webdriver.common.by import By

def test_remove_product_from_cart_list(driver, config):
    logging.info("----- Starting Test C2: Remove Product from Cart on Product List -----")

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(config['username'])
    driver.find_element(By.ID, "password").send_keys(config['password'])
    driver.find_element(By.ID, "login-button").click()

    add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    add_button.click()
    logging.info("Added 'Sauce Labs Bike Light' to cart")

    remove_button = driver.find_element(By.ID, "remove-sauce-labs-bike-light")
    remove_button.click()
    logging.info("Removed 'Sauce Labs Bike Light' from cart")

    cart_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(cart_badge) == 0, "Cart badge should be gone after removing the product"
    logging.info("Cart badge is gone after removal. Product removed successfully.")
