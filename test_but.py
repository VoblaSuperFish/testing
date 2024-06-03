
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By 
from time import sleep
import pytest 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    options = Options()
    #Открыть браузер selenium, но без отображения окна
    options.add_argument('--headless')
    driver=webdriver.Chrome(options=options)    
    return driver

def test_but(driver):
    driver.get('https://www.qa-practice.com/elements/button/simple')
    assert driver.find_element(By.ID, 'submit-id-submit').is_displayed()