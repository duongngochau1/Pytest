import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import test_with_Selenium
class Common():
    def send_keys_Xpath_Locator(locator, data):
        test_with_Selenium.driver.find_element_by_xpath(locator).send_keys(data)

    def send_keys_ID_Locator(locator, data):
        test_with_Selenium.driver.find_element_by_id(locator).send_keys(data)

    def click_Xpath_Locator(locator):
        test_with_Selenium.driver.find_element_by_xpath(locator).click()

    def click_ID_Locator(locator):
        test_with_Selenium.driver.find_element_by_id(locator).click()
