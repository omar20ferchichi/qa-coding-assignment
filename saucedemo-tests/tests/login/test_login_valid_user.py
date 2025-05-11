import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_login_valid_user(driver, config):
    # Extract username and password from the config fixture
    username = config['username']
    password = config['password']

    # Log the beginning of the test
    logging.info("----- Starting Test L1: Login with valid username and password -----")
    logging.info(f"Using credentials: Username: {username} | Password: {password}")

    try:
        # Step 1: Open the login page
        logging.info("Step 1: Navigating to the login page")
        driver.get("https://www.saucedemo.com/")
        logging.info("Login page loaded successfully")

        # Step 2: Enter valid username
        logging.info(f"Step 2: Entering username: {username}")
        username_input = driver.find_element(By.ID, "user-name")
        username_input.send_keys(username)
        logging.info(f"Entered username: {username}")

        # Step 3: Enter valid password
        logging.info(f"Step 3: Entering password: {password}")
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(password)
        logging.info("Entered password")

        # Step 4: Click the login button
        logging.info("Step 4: Clicking the login button")
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        logging.info("Clicked the login button")

        # Step 5: Verify successful login (check if user profile is visible)
        logging.info("Step 5: Verifying successful login")
        try:
            # Wait until the profile icon is present (element specific to the page post-login)
            user_icon = driver.find_element(By.CLASS_NAME, "bm-burger-button")
            assert user_icon.is_displayed(), "User profile icon not displayed!"
            logging.info("Login successful! User profile icon is displayed.")

        except AssertionError as e:
            logging.error(f"Login failed: {e}")
            pytest.fail("Login failed: User profile icon not displayed!")

    except Exception as e:
        logging.error(f"Test failed due to unexpected error: {e}")
        pytest.fail(f"Test failed due to unexpected error: {e}")

    finally:
        logging.info("----- End of Test L1: Login with valid username and password -----")
