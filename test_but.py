
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By 
from time import sleep
import pytest 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    cdp = "C:/Users/HP/Desktop/chromedriver/chromedriver.exe"
    service = Service(executable_path=cdp)
    sleep(2)
    driver=webdriver.Chrome(service=service)    
    return driver

def test_but(driver):
    driver.get('https://www.qa-practice.com/elements/button/simple')
    return driver.find_element(By.ID, 'submit-id-submit').is_displayed()