import pytest
import logging
from selenium.webdriver.common.by import By

def test_image_loading_problem_user(driver):
    logging.info("----- Starting Test P4: Image Load for problem_user -----")

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("problem_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    images = driver.find_elements(By.CLASS_NAME, "inventory_item_img")
    for i, img_container in enumerate(images, 1):
        img = img_container.find_element(By.TAG_NAME, "img")
        src = img.get_attribute("src")
        assert "sl-404" not in src, f"Image {i} appears broken for problem_user"
    logging.info("All product images loaded correctly for problem_user.")
