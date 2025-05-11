import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_u4_footer_elements(driver):
    logging.info("=== Starting Test U4: Footer content and functionality ===")

    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "footer")))

        footer = driver.find_element(By.CLASS_NAME, "footer")
        assert footer.is_displayed()
        logging.info("Footer is visible on the product page.")

        links = footer.find_elements(By.TAG_NAME, "a")
        for link in links:
            href = link.get_attribute("href")
            logging.info(f"Footer link: {href}")
            assert "saucelabs" in href or "twitter" in href or "facebook" in href

    except Exception as e:
        logging.error(f"Test U4 failed: {e}")
        pytest.fail(str(e))

    logging.info("=== End of Test U4 ===")
