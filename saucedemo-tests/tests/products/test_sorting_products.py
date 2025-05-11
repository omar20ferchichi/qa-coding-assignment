import pytest
import logging
from selenium.webdriver.common.by import By

def test_sorting_products(driver, config):
    logging.info("----- Starting Test P5: Sorting Functionality -----")

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(config["username"])
    driver.find_element(By.ID, "password").send_keys(config["password"])
    driver.find_element(By.ID, "login-button").click()

    sort_select = driver.find_element(By.CLASS_NAME, "product_sort_container")
    sort_select.click()

    # A-Z
    sort_select.find_element(By.XPATH, ".//option[text()='Name (A to Z)']").click()
    logging.info("Sorted by Name (A to Z)")

    # Z-A
    sort_select.find_element(By.XPATH, ".//option[text()='Name (Z to A)']").click()
    logging.info("Sorted by Name (Z to A)")

    # Low to High
    sort_select.find_element(By.XPATH, ".//option[text()='Price (low to high)']").click()
    logging.info("Sorted by Price (low to high)")

    # High to Low
    sort_select.find_element(By.XPATH, ".//option[text()='Price (high to low)']").click()
    logging.info("Sorted by Price (high to low)")
