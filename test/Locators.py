import yaml
import sys
import os

test_resource_path = os.path.dirname(__file__)
sys.path.append(test_resource_path)
data = yaml.load(open(test_resource_path +"\\locators.yaml", 'r', encoding='utf-8'), Loader=yaml.FullLoader)

Login_Url = "https://hau.s2retail.online/"
Login_UserName = "usernameOrEmailAddress"
Login_Password = "Password"
Login_Button = "LoginButton"
Login_Failed_Message = "//*[@id=\"listError\"]/span"


MSHP_URL =  data['ManageStoreHomePage']['MSHP_URL']
MSHP_Menu_QLSP_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLSP']
MSHP_Menu_QLSP_SP_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLSP_SP']
MSHP_Menu_QLSP_NCC_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLSP_NCC']
MSHP_Menu_QLSP_KM_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLSP_KM']
MSHP_Menu_QLSP_HH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLSP_HH']
MSHP_Menu_QLSP_TTK_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLSP_TTK']
MSHP_Menu_QLSP_DGCCH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLSP_DGCCH']
MSHP_Menu_QLSP_KKK_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLSP_KKK']
MSHP_Menu_QLKH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLKH']
MSHP_Menu_QLKH_KH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLKH_KH']
MSHP_Menu_QLKH_NKH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLKH_NKH']
MSHP_Menu_QLKH_TKPT_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLKH_TKPT']
MSHP_Menu_QLKH_NTK_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLKH_NTK']
MSHP_Menu_QLKH_GHMH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLKH_GHMH']
MSHP_Menu_QLMH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLMH']
MSHP_Menu_QLMH_MH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLMH_MH']
MSHP_Menu_QLMH_TH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLMH_TH']
MSHP_Menu_QLMH_XK_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLMH_XK']
MSHP_Menu_QLMH_NK_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLMH_NK']
MSHP_Menu_QLMH_LSMH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLMH_LSMH']
MSHP_Menu_QLMH_LSXK_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLMH_LSXK']
MSHP_Menu_QLMH_LSNK_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLMH_LSNK']
MSHP_Menu_QLMH_KP_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLMH_KP']
MSHP_Menu_QLTC_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLTC']
MSHP_Menu_QLTC_HDMH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLTC_HDMH']
MSHP_Menu_QLTC_CNNCC_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLTC_CNNCC']
MSHP_Menu_QLTC_TCTM_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLTC_TCTM']
MSHP_Menu_QLTC_LT_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLTC_LT']
MSHP_Menu_QLTC_NT_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLTC_NT']
MSHP_Menu_QLCH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLCH']
MSHP_Menu_QLCH_CH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLCH_CH']
MSHP_Menu_QLCH_NCH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLCH_NCH']
MSHP_Menu_QLCH_KH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLCH_KH']
MSHP_Menu_QLBH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLBH']
MSHP_Menu_QLBH_BG_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLBH_BG']
MSHP_Menu_QLBH_DDH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLBH_DDH']
MSHP_Menu_QLBH_BH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QLBH_BH']
MSHP_Menu_QT_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QT']
MSHP_Menu_QT_DDBH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QT_DDBH']
MSHP_Menu_QT_NV_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QT_NV']
MSHP_Menu_QT_SHDCT_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QT_SHDCT']
MSHP_Menu_QT_GPSD_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QT_GPSD']
MSHP_Menu_QT_NK_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_QT_NK']
MSHP_Menu_DM_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_DM']
MSHP_Menu_DM_DVT_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_DM_DVT']
MSHP_Menu_DM_TL_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_DM_TL']
MSHP_Menu_DM_GH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_DM_GH']
MSHP_Menu_DM_LD_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_DM_LD']
MSHP_Menu_BC_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_BC']
MSHP_Menu_BC_BCBG_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_BC_BCBG']
MSHP_Menu_BC_MHDH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_BC_MHDH']
MSHP_Menu_BC_DTBH_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_BC_DTBH']
MSHP_Menu_BC_XNT_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_BC_XNT']
MSHP_Menu_CHHT_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_CHHT']
MSHP_Menu_CHWS_LOCATOR = data['ManageStoreHomePage']['MSHP_Menu_CHWS']
MSHP_AppName = data['ManageStoreHomePage']['MSHP_AppName']
MSHP_Notifications_Banner_LOCATOR = data['ManageStoreHomePage']['MSHP_Notifications_Banner']
MSHP_User_Banner_LOCATOR = data['ManageStoreHomePage']['MSHP_User_Banner']
MSHP_User_Profile_Banner_LOCATOR = data['ManageStoreHomePage']['MSHP_User_Profile_Banner']
MSHP_User_Profile_Close_Button_LOCATOR = data['ManageStoreHomePage']['MSHP_User_Profile_Close_Button']

MPP_Product_Search_LOCATOR = 'search-grid'
MPP_Product_Create_Button_LOCATOR = "btnCreateItem"
MPP_Product_Item_Class_Normal_Radio_Button_LOCATOR = 'ItemClass_Normal'
MPP_Product_Item_Class_Matrix_Radio_Button_LOCATOR = 'ItemClass_Matrix'
MPP_Product_Item_Class_Lot_Matrix_Radio_Button_LOCATOR = 'ItemClass_LotMatrix'
MPP_Product_Item_Class_Assembly_Radio_Button_LOCATOR = 'ItemClass_Assembly'
MPP_Product_Create_Product_Button_LOCATOR = 'btnItemClass'
MPP_Product_Close_Create_Product_Button_LOCATOR = "btnCloseIC"
MPP_Product_Create_Product_Tab_General_Info_LOCATOR = "tabCreateNormalItem-tab-1"
MPP_Product_Create_Product_Type_LOCATOR = '//span[@aria-owns="ddlItemType_listbox"]'
MPP_Product_Create_Product_Type_Search_LOCATOR = '//input[@aria-controls="ddlItemType_listbox"]'
MPP_Product_Create_Product_Type_Normal_LOCATOR = '//li[contains(text(), "Chuẩn")]'
MPP_Product_Create_Product_Type_Techology_LOCATOR = '//li[contains(text(), "Kĩ thuật số")]'
MPP_Product_Create_Product_Type_Service_LOCATOR = '//li[contains(text(), "Dịch vụ")]'
MPP_Product_Create_Product_Type_Weight_LOCATOR = '//li[contains(text(), "Trọng lượng")]'
MPP_Product_Create_Product_Type_Sale_Ticket_LOCATOR = '//li[contains(text(), "Phiếu mua hàng")]'
MPP_Product_Create_Product_Code_LOCATOR = 'txtItemCode'
MPP_Product_Create_Product_Name_LOCATOR = 'ItemCreateDto_ItemName'
MPP_Product_Create_Product_Description_LOCATOR = 'txtDescription'
MPP_Product_Create_Product_Department_LOCATOR = '//*[@id="tabGeneralInfor"]/div[3]/div[1]/span'
MPP_Product_Create_Product_Department_Search_LOCATOR = '//*[@id="ddlDepartment-list"]/span/input'
MPP_Product_Create_Product_Category_LOCATOR = '//*[@id="tabGeneralInfor"]/div[3]/div[2]/span'
MPP_Product_Create_Product_Category_Search_LOCATOR = '//*[@id="ddlCategory-list"]/span/input'
MPP_Product_Create_Product_Category_VATTU_LOCATOR = '//*[@id="ddlCategory_listbox"]/li'
MPP_Product_Create_Product_Barcode_Type_LOCATOR = '//*[@id="tabGeneralInfor"]/div[3]/div[3]/span'
MPP_Product_Create_Product_Barcode_Type_Search_LOCATOR = '//*[@id="ddlBarcodeFormat-list"]/span/input'
MPP_Product_Create_Product_Barcode_Code128_LOCATOR = '//*[@id="ddlBarcodeFormat_listbox"]/li[1]'
MPP_Product_Create_Product_Barcode_Code93Extended_LOCATOR = '//*[@id="ddlBarcodeFormat_listbox"]/li[2]'
MPP_Product_Create_Product_Barcode_EAN8_LOCATOR = '//*[@id="ddlBarcodeFormat_listbox"]/li[3]'
MPP_Product_Create_Product_Barcode_UPCA_LOCATOR = '//*[@id="ddlBarcodeFormat_listbox"]/li[4]'
MPP_Product_Create_Product_Barcode_None_LOCATOR = '//*[@id="ddlBarcodeFormat_listbox"]/li[5]'
MPP_Product_Create_Product_Tax_LOCATOR = '//*[@id="tabGeneralInfor"]/div[3]/div[5]/div[1]/span'
MPP_Product_Create_Product_Tax_Search_LOCATOR = '//*[@id="ddlItemTax-list"]/span/input'
MPP_Product_Create_Product_Tax_LI1_LOCATOR = '//*[@id="ddlItemTax_listbox"]/li'
MPP_Product_Create_Product_Tab_Price_LOCATOR = '//*[@id="tabCreateNormalItem-tab-2"]'
MPP_Product_Create_Product_Unit_Of_Measure_LOCATOR = '//*[@id="tabCreateNormalItem-2"]/div/div/div[1]/div[1]/span'
MPP_Product_Create_Product_Unit_Of_Measure_Search_LOCATOR = '//*[@id="ddlUnitOfMeasure-list"]/span/input'
MPP_Product_Create_Product_Unit_Of_Measure_KG_LOCATOR = '//*[@id="ddlUnitOfMeasure_listbox"]/li'
MPP_Product_Create_Product_Net_Price_LOCATOR = '//*[@id="tabCreateNormalItem-2"]/div/div/div[2]/span[1]/span/input[1]'
MPP_Product_Create_Product_Sale_Price_LOCATOR = '//*[@id="tabCreateNormalItem-2"]/div/div/div[3]/span[1]/span/input[1]'
MPP_Product_Create_Product_Price_A_LOCATOR = '//*[@id="tabCreateNormalItem-2"]/div/div/div[5]/span/span/input[1]'
MPP_Product_Create_Product_Price_B_LOCATOR = '//*[@id="tabCreateNormalItem-2"]/div/div/div[6]/span/span/input[1]'
MPP_Product_Create_Product_Price_C_LOCATOR = '//*[@id="tabCreateNormalItem-2"]/div/div/div[7]/span/span/input[1]'
MPP_Product_Create_Product_Tab_Tech_Info_LOCATOR = '//*[@id="tabCreateNormalItem-tab-3"]'
MPP_Product_Create_Product_Parent_Product_LOCATOR = '//*[@id="tabParentItem"]/div/div[1]/div/div[1]/div/div[2]/div[1]/span'
MPP_Product_Create_Product_Parent_Product_Search_LOCATOR = '//*[@id="ddlItem-list"]/span/input'
MPP_Product_Create_Product_Exchange_Value_LOCATOR = '//*[@id="fgExchangeValue"]/span/span/input[1]'
MPP_Product_Create_Product_Size_Length_LOCATOR = '//*[@id="tabParentItem"]/div/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div/span[1]/span/input[1]'
MPP_Product_Create_Product_Size_Width_LOCATOR = '//*[@id="tabParentItem"]/div/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div/span[1]/span/input[1]'
MPP_Product_Create_Product_Size_Height_LOCATOR = '//*[@id="tabParentItem"]/div/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/span[1]/span/input[1]'
MPP_Product_Create_Product_Weight_LOCATOR = '//*[@id="tabParentItem"]/div/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/span[1]/span/input[1]'
MPP_Product_Create_Product_Save_LOCATOR = '//*[@id="toolbarCreateItem"]/a[1]'
MPP_Product_Create_Product_Cancel_LOCATOR = '//*[@id="toolbarCreateItem"]/a[2]'
# MPP_Product_Search_Resulp_First_Row = '//*[@id="gridItem"]/div[3]/table/tbody/tr[1]'
# MPP_Product_Search_Resulp_First_Row_Cell1 = '//*[@id="gridItem"]/div[3]/table/tbody/tr[1]/td[1]/input'
# MPP_Product_Search_Resulp_First_Row_Cell1 = 
# MPP_Product_Search_Resulp_First_Row_Cell1 = 
# MPP_Product_Search_Resulp_First_Row_Cell1 = 
# MPP_Product_Search_Resulp_First_Row_Cell1 = 