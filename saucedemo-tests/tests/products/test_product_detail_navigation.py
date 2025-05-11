import pytest
import logging
from selenium.webdriver.common.by import By

def test_product_detail_navigation(driver, config):
    logging.info("----- Starting Test P6: Product Detail Navigation -----")

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(config["username"])
    driver.find_element(By.ID, "password").send_keys(config["password"])
    driver.find_element(By.ID, "login-button").click()

    first_product = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    product_name = first_product.text
    first_product.click()

    detail_header = driver.find_element(By.CLASS_NAME, "inventory_details_name")
    assert detail_header.text == product_name, "Product name on detail page does not match"
    logging.info(f"Successfully navigated to detail page for: {product_name}")
