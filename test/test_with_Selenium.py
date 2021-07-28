import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import Data
from Common import Common
import Locators

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


def loadPage():
    chrome_open
    driver.get(Locators.Login_Url)
    
def login():
    Common.send_keys_ID_Locator(Locators.Login_UserName, Data.Login_UserName)
    Common.send_keys_ID_Locator(Locators.Login_Password, Data.Login_Password)
    Common.click_ID_Locator(Locators.Login_Button)


def test_ThemSP_ThongtinChung():
    loadPage()
    login()
    time.sleep(3)
    Common.click_Xpath_Locator(Locators.MSHP_Menu_QLSP_LOCATOR)

    Common.click_Xpath_Locator(Locators.MSHP_Menu_QLSP_SP_LOCATOR)

    time.sleep(1)
    Common.click_ID_Locator(Locators.MPP_Product_Create_Button_LOCATOR)
    time.sleep(2)
    Common.click_ID_Locator(Locators.MPP_Product_Create_Product_Button_LOCATOR)

    #điền thông tin SP
    driver.find_element_by_xpath(Locators.MPP_Product_Create_Product_Type_LOCATOR).click()

    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Type_Normal_LOCATOR)

    Common.send_keys_ID_Locator(Locators.MPP_Product_Create_Product_Code_LOCATOR, "SP0005")

    Common.send_keys_ID_Locator(Locators.MPP_Product_Create_Product_Name_LOCATOR, "Sản phẩm 45")

    Common.send_keys_ID_Locator(Locators.MPP_Product_Create_Product_Description_LOCATOR, "Đây là sản phẩm 5")

    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Department_LOCATOR)
    Common.click_Xpath_Locator()

    time.sleep(3)
    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Category_LOCATOR)
    time.sleep(1)
    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Category_VATTU_LOCATOR)

    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Barcode_Type_LOCATOR)
    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Barcode_Code128_LOCATOR)

    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Tax_LOCATOR)
    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Tax_LI1_LOCATOR)


    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Tab_Price_LOCATOR)

    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Unit_Of_Measure_LOCATOR)

    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Unit_Of_Measure_KG_LOCATOR)

    Common.send_keys_Xpath_Locator(Locators.MPP_Product_Create_Product_Net_Price_LOCATOR,"240000")

    Common.send_keys_Xpath_Locator(Locators.MPP_Product_Create_Product_Sale_Price_LOCATOR, "250000")

    Common.send_keys_Xpath_Locator(Locators.MPP_Product_Create_Product_Price_A_LOCATOR, "245000")

    Common.send_keys_Xpath_Locator(Locators.MPP_Product_Create_Product_Price_B_LOCATOR, "255000")

#    Common.send_keys_Xpath_Locator(Locators.MPP_Product_Create_Product_Price_C_LOCATOR, "260000")

    Common.click_Xpath_Locator('//*[@id="bodyContent"]/div/div[1]/div/div/h5')
    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Save_LOCATOR)



