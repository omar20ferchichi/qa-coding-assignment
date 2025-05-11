import pytest
import logging
from selenium.webdriver.common.by import By

def test_e3_repeated_invalid_login(driver):
    logging.info("=== Starting Test E3: Repeated invalid login attempts ===")
    try:
        for i in range(3):
            driver.get("https://www.saucedemo.com/")
            driver.find_element(By.ID, "user-name").clear()
            driver.find_element(By.ID, "password").clear()
            driver.find_element(By.ID, "user-name").send_keys("invalid_user")
            driver.find_element(By.ID, "password").send_keys("wrong_password")
            driver.find_element(By.ID, "login-button").click()

            error = driver.find_element(By.CLASS_NAME, "error-message-container")
            assert error.is_displayed()
            logging.info(f"Attempt {i+1}: Login failed as expected.")

    except Exception as e:
        logging.error(f"Test E3 failed: {e}")
        pytest.fail(str(e))
    logging.info("=== End of Test E3 ===")
