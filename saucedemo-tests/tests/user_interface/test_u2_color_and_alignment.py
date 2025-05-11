import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_u2_color_and_alignment(driver):
    logging.info("=== Starting Test U2: Color consistency and alignment of elements ===")

    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

        buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for btn in buttons:
            color = btn.value_of_css_property("background-color")
            logging.info(f"Button color: {color}")
            assert "rgba" in color or "#" in color

        first_card = driver.find_element(By.CLASS_NAME, "inventory_item")
        alignment = first_card.value_of_css_property("text-align")
        logging.info(f"Card alignment: {alignment}")
        assert alignment in ["left", "start"]

    except Exception as e:
        logging.error(f"Test U2 failed: {e}")
        pytest.fail(str(e))

    logging.info("=== End of Test U2 ===")
