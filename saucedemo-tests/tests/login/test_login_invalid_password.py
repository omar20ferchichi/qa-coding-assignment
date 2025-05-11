import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_login_invalid_password(driver, config):
    username = config['username']
    password = "invalid_password"
    
    logging.info("----- Starting Test L6: Login with invalid password -----")
    logging.info(f"Using credentials: Username: {username} | Password: {password}")

    try:
        # Step 1: Open the login page
        driver.get("https://www.saucedemo.com/")
        logging.info("Login page loaded successfully")

        # Step 2: Enter valid username
        logging.info(f"Step 2: Entering username: {username}")
        username_input = driver.find_element(By.ID, "user-name")
        username_input.send_keys(username)
        logging.info(f"Entered username: {username}")

        # Step 3: Enter invalid password
        logging.info(f"Step 3: Entering password: {password}")
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(password)
        logging.info("Entered password")

        # Step 4: Click login button
        logging.info("Step 4: Clicking the login button")
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Step 5: Verify error message for invalid password
        logging.info("Step 5: Verifying error message for invalid password")
        error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        assert error_message.is_displayed(), "Error message not displayed!"
        logging.info("Error message for invalid password displayed as expected.")


    except Exception as e:
            logging.error(f"Test failed due to unexpected error: {e}")
            pytest.fail(f"Test failed due to unexpected error: {e}")

    finally:
        logging.info("----- End of Test L6: Login with invalid password -----")
