import pytest
import logging
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Initialize variable for the logs folder path
logs_folder_path = ""

def pytest_sessionstart(session):
    """Create a time-stamped log folder before the session starts."""
    global logs_folder_path
    date_str = datetime.now().strftime("%Y-%m-%d_%H")
    logs_folder_path = os.path.join("logs", date_str)

    # Ensure the log folder exists
    os.makedirs(logs_folder_path, exist_ok=True)

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """Configure logging for each test in the correct log folder."""
    global logs_folder_path
    test_file = item.fspath.basename.replace(".py", "")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = os.path.join(logs_folder_path, f"{test_file}_{timestamp}.log")

    # Remove previous logging handlers to avoid duplicates
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Set up logging to the log file
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info(f"--- Starting test: {item.name} ---")

@pytest.fixture
def driver():
    """Initialize and quit Chrome WebDriver."""
    # chrome_options = Options()
    # chrome_options.add_argument("--headless=new")              # Run Chrome in headless mode
    # chrome_options.add_argument("--no-sandbox")                # Bypass OS security model (needed for Docker)
    # chrome_options.add_argument("--disable-dev-shm-usage")     # Avoid shared memory issues
    # chrome_options.add_argument("--disable-gpu")               # Optional but good in headless
    # chrome_options.add_argument("--window-size=1920,1080")     # Set default window size
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def config():
    """Return default test credentials."""
    return {
        "username": "standard_user",
        "password": "secret_sauce"
    }
