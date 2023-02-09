import pytest 

from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

@pytest.mark.skip("причина пропуска")
def test_positive_auth(driver):
    #открываем url авторизации
    driver.get("https://www.saucedemo.com/")

    #находим поле ввода username используя xpath
    username = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username.clear()
    username.send_keys("standard_user")

    password = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password.clear()
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    #ждем 10 секунд 
    sleep(10)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

    #закрываем окно браузера
    driver.close()
    
@pytest.mark.skip("причина пропуска")
def test_invalid_auth(driver):
    #открываем url авторизации
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username.clear()
    username.send_keys("locked_out_user")

    password = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password.clear()
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    sleep(10)
    assert driver.current_url == 'https://www.saucedemo.com/'

    #закрываем окно браузера
    driver.close()


@pytest.mark.skip("причина пропуска")
def test_random_auth_data(driver):
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username.clear()
    username.send_keys("okokokokok")

    password = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password.clear()
    password.send_keys("kmmkkmkmkmkm")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    sleep(10)
    error = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
    assert error.text == "Epic sadface: Username and password do not match any user in this service"
    assert driver.current_url == 'https://www.saucedemo.com/'

    #закрываем окно браузера
    driver.close()  


@pytest.mark.skip("причина пропуска")
def test_auth_glitch_user(driver):
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username.clear()
    username.send_keys("performance_glitch_user")

    password = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password.clear()
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    sleep(10)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

    #закрываем окно браузера
    driver.close()      


@pytest.mark.skip("причина пропуска")
def test_empty_fields_auth(driver):
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username.clear()
    

    password = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password.clear()
    

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    sleep(10)
    error = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
    assert error.text == "Epic sadface: Username is required"
    assert driver.current_url == 'https://www.saucedemo.com/'

    #закрываем окно браузера
    driver.close()  


def test_empty_fields_auth(driver):
    driver.get("https://www.saucedemo.com/")
    
    text1 = """
    Accepted usernames are:
    standard_user
    locked_out_user
    problem_user
    performance_glitch_user"""
    
    searchedtext = driver.find_element(By.XPATH, '//div[contains(text(), "standard_user")]')
    text = searchedtext.text

    assert text == text1

    print(text)


    
    #закрываем окно браузера
    driver.close()  