import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_login_performance_glitch_user(driver, config):
    username = "performance_glitch_user"
    password = config['password']
    
    logging.info("----- Starting Test L4: Login with performance glitch user -----")
    logging.info(f"Using credentials: Username: {username} | Password: {password}")

    try:
        # Step 1: Open the login page
        driver.get("https://www.saucedemo.com/")
        logging.info("Login page loaded successfully")

        # Step 2: Enter valid username for performance glitch user
        logging.info(f"Step 2: Entering username: {username}")
        username_input = driver.find_element(By.ID, "user-name")
        username_input.send_keys(username)
        logging.info(f"Entered username: {username}")

        # Step 3: Enter valid password
        logging.info(f"Step 3: Entering password: {password}")
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(password)
        logging.info("Entered password")

        # Step 4: Click login button
        logging.info("Step 4: Clicking the login button")
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Step 5: Verify if page loads with performance glitches
        logging.info("Step 5: Verifying page for performance glitches")
        page_load = driver.find_element(By.CLASS_NAME, "inventory_container")
        assert page_load.is_displayed(), "Page load failed with performance glitches!"
        logging.info("Page loaded successfully despite performance glitches.")

    except Exception as e:
        logging.error(f"Test failed due to unexpected error: {e}")
        pytest.fail(f"Test failed due to unexpected error: {e}")

    finally:
        logging.info("----- End of Test L4: Login with performance glitch user -----")
