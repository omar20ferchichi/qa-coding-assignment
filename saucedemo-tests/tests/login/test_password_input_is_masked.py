import pytest
import logging
from selenium.webdriver.common.by import By

def test_password_input_is_masked(driver):
    logging.info("----- Starting Test L9: Check if password input is masked -----")

    try:
        password_input = driver.find_element(By.ID, "password")
        input_type = password_input.get_attribute("type")

        assert input_type == "password", f"Expected input type 'password', got '{input_type}'"
        logging.info("Password field is masked correctly")

    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        pytest.fail(str(e))

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        pytest.fail(str(e))

    finally:
        logging.info("----- End of Test L9 -----")
