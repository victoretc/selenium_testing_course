import pytest 

from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from time import sleep

@pytest.fixture()
def get_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    #options.add_argument('chrome')
    options.add_argument('--start-maximized')
    return options


@pytest.fixture()
def driver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def test_first(driver):
    driver.get("https://www.saucedemo.com/")
    sleep(3)
    driver.close()

