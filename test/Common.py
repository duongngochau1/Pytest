import Config
import Data
import Locators


class Common():
    def loadPage():
        Config.chrome_open
        Config.driver.get(Locators.Login_Url)

    def login():
        Common.send_keys_ID_Locator(Locators.Login_UserName, Data.Login_UserName)
        Common.send_keys_ID_Locator(Locators.Login_Password, Data.Login_Password)
        Common.click_ID_Locator(Locators.Login_Button)

    def send_keys_Xpath_Locator(locator, data):
        Config.driver.find_element_by_xpath(locator).send_keys(data)

    def send_keys_ID_Locator(locator, data):
        Config.driver.find_element_by_id(locator).send_keys(data)

    def click_Xpath_Locator(locator):
        Config.driver.find_element_by_xpath(locator).click()

    def click_ID_Locator(locator):
        Config.driver.find_element_by_id(locator).click()
