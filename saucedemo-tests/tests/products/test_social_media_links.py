import pytest
import logging
from selenium.webdriver.common.by import By

def test_social_media_links(driver, config):
    logging.info("----- Starting Test P7: Social Media Links -----")

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(config["username"])
    driver.find_element(By.ID, "password").send_keys(config["password"])
    driver.find_element(By.ID, "login-button").click()

    twitter = driver.find_element(By.CLASS_NAME, "social_twitter")
    facebook = driver.find_element(By.CLASS_NAME, "social_facebook")
    linkedin = driver.find_element(By.CLASS_NAME, "social_linkedin")

    assert twitter.is_displayed()
    assert facebook.is_displayed()
    assert linkedin.is_displayed()
    logging.info("Social media icons (Twitter, Facebook, LinkedIn) are displayed.")
