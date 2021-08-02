import time

from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


import Data
from Common import Common
import Locators
import Config


def test_ThemSP_ThongtinChung():
    Common.loadPage()
    Common.login()
    time.sleep(3)
    Common.click_Xpath_Locator(Locators.MSHP_Menu_QLSP_LOCATOR)
    time.sleep(1)
    Common.click_Xpath_Locator(Locators.MSHP_Menu_QLSP_SP_LOCATOR)

    time.sleep(2)
    Common.click_ID_Locator(Locators.MPP_Product_Create_Button_LOCATOR)
    time.sleep(2)
    Common.click_ID_Locator(Locators.MPP_Product_Create_Product_Button_LOCATOR)

    time.sleep(3)
    Config.driver.find_element_by_xpath(Locators.MPP_Product_Create_Product_Type_LOCATOR).click()
    time.sleep(1)
    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Type_Normal_LOCATOR)

    Common.send_keys_ID_Locator(Locators.MPP_Product_Create_Product_Code_LOCATOR, "SP0010")

    Common.send_keys_ID_Locator(Locators.MPP_Product_Create_Product_Name_LOCATOR, "Sản phẩm 10")

    Common.send_keys_ID_Locator(Locators.MPP_Product_Create_Product_Description_LOCATOR, "Đây là sản phẩm 10")
    time.sleep(1)
    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Department_LOCATOR)
    time.sleep(1)
    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Department_Item1_LOCATOR)

    time.sleep(1)
    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Category_LOCATOR)
    time.sleep(1)
    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Category_VATTU_LOCATOR)

    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Barcode_Type_LOCATOR)
    time.sleep(1)
    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Barcode_Code128_LOCATOR)

    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Tax_LOCATOR)
    time.sleep(1)
    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Tax_LI1_LOCATOR)
    time.sleep(1)
    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Tab_Price_LOCATOR)
    time.sleep(1)
    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Unit_Of_Measure_LOCATOR)

    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Unit_Of_Measure_KG_LOCATOR)

    Common.send_keys_Xpath_Locator(Locators.MPP_Product_Create_Product_Net_Price_LOCATOR,"240000")
    time.sleep(1)
    Common.send_keys_Xpath_Locator(Locators.MPP_Product_Create_Product_Sale_Price_LOCATOR, "250000")
    time.sleep(1)
    Common.send_keys_Xpath_Locator(Locators.MPP_Product_Create_Product_Price_A_LOCATOR, "245000")
    time.sleep(1)
    Common.send_keys_Xpath_Locator(Locators.MPP_Product_Create_Product_Price_B_LOCATOR, "255000")

#    Common.send_keys_Xpath_Locator(Locators.MPP_Product_Create_Product_Price_C_LOCATOR, "260000")
    time.sleep(1)
    Common.click_Xpath_Locator('//div[@class="s2-switch"]')
    time.sleep(1)
    Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Save_LOCATOR)



