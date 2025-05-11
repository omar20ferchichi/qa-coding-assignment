import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import time


# Utility function to calculate total price (item total + tax)
def calculate_total_price(item_prices):
    item_total = sum(item_prices)
    tax = item_total * 0.08  # 8% tax
    return item_total + tax


# Helper function to get the current timestamp for logs
def get_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())


def test_checkout_process(driver, config):
    username = config['username']
    password = config['password']

    # Start of the test
    logging.info(f"==================== TEST STARTED ====================")
    logging.info(f"Test started at: {get_timestamp()}")
    logging.info(f"Test Name: Checkout Process Test")

    try:
        # Step 1: Log into the site
        start_time = time.time()
        logging.info(f"[{get_timestamp()}] Step 1: Logging in with credentials")
        
        driver.get("https://www.saucedemo.com/")
        username_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        sleep(2)  # Wait for login to complete
        elapsed_time = time.time() - start_time
        logging.info(f"[{get_timestamp()}] Step 1 completed in {elapsed_time:.2f} seconds")
        logging.info(f"Logged in successfully")

        # Step 2: Sort items by lowest price
        start_time = time.time()
        logging.info(f"[{get_timestamp()}] Step 2: Sorting items by lowest price")
        sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        sort_dropdown.click()
        sort_dropdown.find_element(By.XPATH, "//option[@value='lohi']").click()
        sleep(2)  # Wait for items to reload with new sorting
        elapsed_time = time.time() - start_time
        logging.info(f"[{get_timestamp()}] Step 2 completed in {elapsed_time:.2f} seconds")
        logging.info("Sorted items by price (Lowest to Highest)")

        # Step 3: Add two or more items to the shopping cart
        start_time = time.time()
        logging.info(f"[{get_timestamp()}] Step 3: Adding two items to the cart")
        item_prices = []
        for i in range(2):  # Add first two items
            item = driver.find_elements(By.CLASS_NAME, "inventory_item")[i]
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            item_prices.append(float(price.strip('$')))
            add_to_cart_button = item.find_element(By.CLASS_NAME, "btn_inventory")
            add_to_cart_button.click()
            sleep(1)  # Wait for item to be added to the cart
        elapsed_time = time.time() - start_time
        logging.info(f"[{get_timestamp()}] Step 3 completed in {elapsed_time:.2f} seconds")
        logging.info(f"Added two items to the cart")

        # Step 4: Visit the shopping cart
        start_time = time.time()
        logging.info(f"[{get_timestamp()}] Step 4: Navigating to the shopping cart")
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        sleep(2)  # Wait for cart page to load
        elapsed_time = time.time() - start_time
        logging.info(f"[{get_timestamp()}] Step 4 completed in {elapsed_time:.2f} seconds")

        # Step 5: Assert that the items in the cart are correct
        start_time = time.time()
        logging.info(f"[{get_timestamp()}] Step 5: Verifying items in the cart")
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 2, f"Cart does not contain the correct number of items"
        cart_item_prices = [
            float(item.find_element(By.CLASS_NAME, "inventory_item_price").text.strip('$'))
            for item in cart_items
        ]
        assert cart_item_prices == item_prices, "Prices in the cart do not match the selected items"
        elapsed_time = time.time() - start_time
        logging.info(f"[{get_timestamp()}] Step 5 completed in {elapsed_time:.2f} seconds")
        logging.info("Verified correct items in the cart")

        # Step 6: Proceed to Checkout
        start_time = time.time()
        logging.info(f"[{get_timestamp()}] Step 6: Clicking on Checkout button")
        checkout_button = driver.find_element(By.CLASS_NAME, "checkout_button")
        checkout_button.click()
        sleep(2)  # Wait for checkout page to load
        elapsed_time = time.time() - start_time
        logging.info(f"[{get_timestamp()}] Step 6 completed in {elapsed_time:.2f} seconds")

        # Step 7: Fill in Checkout details
        start_time = time.time()
        logging.info(f"[{get_timestamp()}] Step 7: Filling in checkout details")
        first_name_input = driver.find_element(By.ID, "first-name")
        last_name_input = driver.find_element(By.ID, "last-name")
        postal_code_input = driver.find_element(By.ID, "postal-code")

        first_name_input.send_keys("John")
        last_name_input.send_keys("Doe")
        postal_code_input.send_keys("12345")

        continue_button = driver.find_element(By.CLASS_NAME, "cart_button")
        continue_button.click()
        sleep(2)  # Wait for the checkout overview page
        elapsed_time = time.time() - start_time
        logging.info(f"[{get_timestamp()}] Step 7 completed in {elapsed_time:.2f} seconds")

        # Step 8: Assert purchasing correct items
        start_time = time.time()
        logging.info(f"[{get_timestamp()}] Step 8: Verifying purchased items in checkout overview")
        checkout_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        assert len(checkout_items) == 2, f"Checkout does not show the correct number of items"
        elapsed_time = time.time() - start_time
        logging.info(f"[{get_timestamp()}] Step 8 completed in {elapsed_time:.2f} seconds")

        # Step 9: Assert the total price
        start_time = time.time()
        logging.info(f"[{get_timestamp()}] Step 9: Verifying total price calculation")
        item_total = sum(item_prices)
        expected_tax = item_total * 0.08
        expected_total = item_total + expected_tax

        total_price = driver.find_element(By.CLASS_NAME, "summary_total_label").text
        total_price = float(total_price.strip("Total: $"))
        assert total_price == expected_total, f"Total price is incorrect! Expected {expected_total}, but got {total_price}"
        elapsed_time = time.time() - start_time
        logging.info(f"[{get_timestamp()}] Step 9 completed in {elapsed_time:.2f} seconds")
        logging.info(f"Verified total price: {total_price}")

        # Step 10: Finish checkout and assert empty cart
        start_time = time.time()
        logging.info(f"[{get_timestamp()}] Step 10: Finishing checkout")
        finish_button = driver.find_element(By.CLASS_NAME, "cart_checkout_link")
        finish_button.click()
        sleep(2)  # Wait for confirmation page
        elapsed_time = time.time() - start_time
        logging.info(f"[{get_timestamp()}] Step 10 completed in {elapsed_time:.2f} seconds")

        # Step 11: Assert cart is empty
        start_time = time.time()
        logging.info(f"[{get_timestamp()}] Step 11: Verifying cart is empty after checkout")
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 0, "Cart is not empty after checkout"
        elapsed_time = time.time() - start_time
        logging.info(f"[{get_timestamp()}] Step 11 completed in {elapsed_time:.2f} seconds")

    except Exception as e:
        logging.error(f"[{get_timestamp()}] Test failed due to: {e}")
        pytest.fail(f"Test failed: {e}")

    logging.info(f"==================== TEST FINISHED ====================")
    logging.info(f"Test ended at: {get_timestamp()}")
