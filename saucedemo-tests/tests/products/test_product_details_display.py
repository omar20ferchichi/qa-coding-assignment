import pytest
import logging
from selenium.webdriver.common.by import By

def test_product_details_display(driver, config):
    logging.info("----- Starting Test P3: Product Details Display -----")

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(config["username"])
    driver.find_element(By.ID, "password").send_keys(config["password"])
    driver.find_element(By.ID, "login-button").click()

    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for i, product in enumerate(products, 1):
        name = product.find_element(By.CLASS_NAME, "inventory_item_name")
        img = product.find_element(By.CLASS_NAME, "inventory_item_img")
        price = product.find_element(By.CLASS_NAME, "inventory_item_price")
        assert name.is_displayed(), f"Product {i}: Name not displayed"
        assert img.is_displayed(), f"Product {i}: Image not displayed"
        assert price.is_displayed(), f"Product {i}: Price not displayed"
    logging.info("All products have name, image, and price displayed.")
