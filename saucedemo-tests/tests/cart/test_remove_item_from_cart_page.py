import pytest
import logging
from selenium.webdriver.common.by import By

def test_remove_item_from_cart_page(driver, config):
    logging.info("----- Starting Test C5: Remove Item from Cart Page -----")

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(config['username'])
    driver.find_element(By.ID, "password").send_keys(config['password'])
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 0, "Cart should be empty after item removal"
    logging.info("Item successfully removed from the cart page.")
