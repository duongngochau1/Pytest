import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

@pytest.fixture(autouse="true")
def chrome_open():
    global driver
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    time.sleep(10)
    driver.close()
    driver.quit()
    print('Test completed')
