import os
import time
import sys

sys.path.append(os.path.dirname(__file__).replace('test', 'Resource'))
sys.path.append(os.path.dirname(__file__))


def test_ThemSP_ThongtinChung():
    Common.loadPage()
    Common.login()
    Create_Produce_Normal.Click_Menu_Produce()

    Create_Produce_Normal.Click_Create_Produce_Create_Button()

    Create_Produce_Normal.Click_Create_Produce_Type()

    Create_Produce_Normal.Sendkey_Create_Produce_Code()

    Create_Produce_Normal.Sendkey_Create_Produce_Name()

    Create_Produce_Normal.Sendkey_Create_Produce_Description()

    Create_Produce_Normal.Click_Create_Produce_Department()

    Create_Produce_Normal.Click_Create_Produce_Category()

    Create_Produce_Normal.Click_Create_Produce_Barcode_Type()

    Create_Produce_Normal.Click_Create_Produce_Tax()

    Create_Produce_Normal.Click_Create_Produce_Tab_Price()

    Create_Produce_Normal.Click_Create_Produce_Unit_Of_Measure()

    Create_Produce_Normal.Sendkey_Create_Produce_Net_Price()

    Create_Produce_Normal.Sendkey_Create_Produce_Sale_Price()

    Create_Produce_Normal.Sendkey_Create_Produce_Price_A()

    Create_Produce_Normal.Sendkey_Create_Produce_Price_B()

    Create_Produce_Normal.Click_Create_Produce_Save_Button()
