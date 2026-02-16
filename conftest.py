import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

@pytest.fixture(scope="session")
def setup_webdriver():
    if os.getenv("BROWSER")=="chrome":
        driver = setup_chrome_driver()
    elif os.getenv("BROWSER")=="firefox":
        driver = setup_firefox_driver()
    else:
        raise Exception("Invalid Env Value passed")
    yield driver
    driver.quit()


def setup_chrome_driver():
    options = webdriver.ChromeOptions()
    if os.getenv("HEADLESS") == "true":
        options.add_argument("headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver

def setup_firefox_driver():
    options = webdriver.FirefoxOptions()
    if os.getenv("HEADLESS") == "true":
        options.add_argument("headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    return driver

