import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_login_problem_user(driver, config):
    username = "problem_user"
    password = config['password']
    
    logging.info("----- Starting Test L3: Login with problem user -----")
    logging.info(f"Using credentials: Username: {username} | Password: {password}")

    try:
        # Step 1: Open the login page
        driver.get("https://www.saucedemo.com/")
        logging.info("Login page loaded successfully")

        # Step 2: Enter valid username for problem user
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

        # Step 5: Check for UI issues or missing elements (like product image)
        logging.info("Step 5: Verifying product image or UI issues")
        try:
            product_image = driver.find_element(By.CLASS_NAME, "inventory_item_img")
            assert product_image.is_displayed(), "Product image not displayed!"
            logging.info("Product image displayed correctly.")
        except Exception as e:
            logging.error(f"UI issue detected: {e}")

    except Exception as e:
        logging.error(f"Test failed due to unexpected error: {e}")
        pytest.fail(f"Test failed due to unexpected error: {e}")

    finally:
        logging.info("----- End of Test L3: Login with problem user -----")
