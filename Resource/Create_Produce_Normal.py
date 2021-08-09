import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

import Data
from Common import Common
import Locators
import Config

class Create_Produce_Normal(Common):
    def Click_Menu_Produce(self):
        time.sleep(3)
        self.click_Xpath_Locator(Locators.MSHP_Menu_QLSP_LOCATOR)
        time.sleep(1)
        self.click_Xpath_Locator(Locators.MSHP_Menu_QLSP_SP_LOCATOR)

    def Click_Create_Produce_Create_Button(self):
        time.sleep(2)
        Common.click_ID_Locator(Locators.MPP_Product_Create_Button_LOCATOR)
        time.sleep(2)
        Common.click_ID_Locator(Locators.MPP_Product_Create_Product_Button_LOCATOR)
        
    def Click_Create_Produce_Type(self):
        time.sleep(2)
        Config.driver.find_element_by_xpath(Locators.MPP_Product_Create_Product_Type_LOCATOR).click()
        time.sleep(1)
        Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Type_Normal_LOCATOR)

    def Sendkey_Create_Produce_Code(self):
        Common.send_keys_ID_Locator(Locators.MPP_Product_Create_Product_Code_LOCATOR, "SP0010")

    def Sendkey_Create_Produce_Name(self):
        Common.send_keys_ID_Locator(Locators.MPP_Product_Create_Product_Name_LOCATOR, "Sản phẩm 10")

    def Sendkey_Create_Produce_Description(self):
        Common.send_keys_ID_Locator(Locators.MPP_Product_Create_Product_Description_LOCATOR, "Đây là sản phẩm 10")

    def Click_Create_Produce_Department(self):
        time.sleep(1)
        Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Department_LOCATOR)
        time.sleep(1)
        Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Department_Item1_LOCATOR)

    def Click_Create_Produce_Category(self):
        time.sleep(1)
        Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Category_LOCATOR)
        time.sleep(1)
        Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Category_VATTU_LOCATOR)

    def Click_Create_Produce_Barcode_Type(self):
        Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Barcode_Type_LOCATOR)
        time.sleep(1)
        Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Barcode_Code128_LOCATOR)

    def Click_Create_Produce_Tax(self):
        time.sleep(1)
        Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Tax_LOCATOR)
        time.sleep(1)
        Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Tax_LI1_LOCATOR)

    def Click_Create_Produce_Tab_Price(self):
        time.sleep(1)
        Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Tab_Price_LOCATOR)

    def Click_Create_Produce_Unit_Of_Measure(self):
        time.sleep(1)
        Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Unit_Of_Measure_LOCATOR)
        time.sleep(1)
        Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Unit_Of_Measure_KG_LOCATOR)

    def Sendkey_Create_Produce_Net_Price(self):
        time.sleep(1)
        Common.send_keys_Xpath_Locator(Locators.MPP_Product_Create_Product_Net_Price_LOCATOR, "240000")

    def Sendkey_Create_Produce_Sale_Price(self):
        time.sleep(1)
        Common.send_keys_Xpath_Locator(Locators.MPP_Product_Create_Product_Sale_Price_LOCATOR, "250000")

    def Sendkey_Create_Produce_Price_A(self):
        time.sleep(1)
        Common.send_keys_Xpath_Locator(Locators.MPP_Product_Create_Product_Price_A_LOCATOR, "245000")
        time.sleep(1)

    def Sendkey_Create_Produce_Price_B(self):
        Common.send_keys_Xpath_Locator(Locators.MPP_Product_Create_Product_Price_B_LOCATOR, "255000")

        #    Common.send_keys_Xpath_Locator(Locators.MPP_Product_Create_Product_Price_C_LOCATOR, "260000")
    def Click_Create_Produce_Save_Button(self):
        time.sleep(1)
        Common.click_Xpath_Locator('//div[@class="s2-switch"]')
        time.sleep(1)
        Common.click_Xpath_Locator(Locators.MPP_Product_Create_Product_Save_LOCATOR)
