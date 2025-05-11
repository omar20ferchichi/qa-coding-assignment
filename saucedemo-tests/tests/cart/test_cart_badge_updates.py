import pytest
import logging
from selenium.webdriver.common.by import By

def test_cart_badge_updates(driver, config):
    logging.info("----- Starting Test C6: Cart Badge Updates Correctly -----")

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(config['username'])
    driver.find_element(By.ID, "password").send_keys(config['password'])
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1", "Cart badge should show 1"

    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0, "Cart badge should disappear"
    logging.info("Cart badge correctly updates on add and remove.")
