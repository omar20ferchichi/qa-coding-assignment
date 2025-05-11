import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_u1_responsive_design(driver):
    logging.info("=== Starting Test U1: Responsive design across screen sizes ===")
    sizes = [(1920, 1080), (1366, 768), (768, 1024), (375, 667)]  # Desktop, tablet, mobile

    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

        for width, height in sizes:
            driver.set_window_size(width, height)
            logging.info(f"Set screen size to {width}x{height}")
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

            assert driver.find_element(By.CLASS_NAME, "inventory_list").is_displayed()
            logging.info("Product list visible at this screen size.")

    except Exception as e:
        logging.error(f"Test U1 failed: {e}")
        pytest.fail(str(e))

    logging.info("=== End of Test U1 ===")
