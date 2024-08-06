import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pytest_bdd import scenarios, given, when, then, parsers
import time

# Constants
TIMEOUT = 4
URL = 'https://www.saucedemo.com/'
# Update this path to your chromedriver executable

# Scenarios
scenarios('../features/tc01.feature')

# Fixtures
@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(TIMEOUT)
    driver.maximize_window()
    yield driver
    driver.quit()

# Given Steps
@given('User is on login page')
def open_browser(driver):
    driver.get(URL)

# When Steps
@when(parsers.parse('User enter username "{username}" and password "{password}"'))
def login(driver, username, password):
    driver.find_element(By.ID, 'user-name').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    
    driver.find_element(By.ID, 'login-button').click()

# Then Steps
@then('User should be able to login successfully and new page open "Swag Labs"')
def add_to_cart(driver):
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click() 
    driver.find_element(By.XPATH, '//div[@id="shopping_cart_container"]').click()
    page_source = driver.page_source

# Check if the text is present in the page source
    if "Sauce Labs Backpack" in page_source:
        print('Text "Sauce Labs Backpack" is present on the page.')
        driver.close()
    else:
        print('Text "Sauce Labs Backpack" is not present on the page.')
        
        


     


