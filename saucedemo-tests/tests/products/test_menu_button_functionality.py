import pytest
import logging
from selenium.webdriver.common.by import By

def test_menu_button_functionality(driver, config):
    logging.info("----- Starting Test P8: Menu Button Toggle -----")

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(config["username"])
    driver.find_element(By.ID, "password").send_keys(config["password"])
    driver.find_element(By.ID, "login-button").click()

    menu_btn = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_btn.click()
    logging.info("Menu opened.")
    
    assert driver.find_element(By.CLASS_NAME, "bm-menu-wrap").is_displayed()
    
    close_btn = driver.find_element(By.ID, "react-burger-cross-btn")
    close_btn.click()
    logging.info("Menu closed.")
