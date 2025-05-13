import re
import pytest
from Pages.MainPage import MainPage
from Pages.Elements_Page import ElementsPage
from Pages.CheckBoxPage import CheckBoxPage
from Configuration.TestData import TestData
from Configuration.log_config import *



@pytest.mark.usefixtures("driver_Setup")
class Test_CheckBoxPage():
    """Test Check Box page elements"""
    driver = None
    
    d_logger = get_debug_logger_()

    @pytest.mark.CheckBoxTitle
    def test_checkboxtitle(self,driver_Setup):    
        """Checks the Check Box title is displayed"""
        self.driver = driver_Setup
        self.driver.get(TestData.url)
        mainp =MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        checkBoxPage= CheckBoxPage(self.driver)
        mainp.click_elements_page()
        elements_page.click_check_box_text()
        checkBoxPage.click_expand_all()
        texto = checkBoxPage.get_check_box_title().text
        assert texto == "Check Box"
        self.d_logger.info(f"Check Box title done : {texto}")
        

    @pytest.mark.ChecBoxDesktop
    def test_desktop_menu_present(self,driver_Setup):
        """Checks the Desktop menu option is dispplayed"""
        self.driver = driver_Setup
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        checkBoxPage= CheckBoxPage(self.driver)
        mainp.click_elements_page()
        elements_page.click_check_box()
        checkBoxPage.click_expand_all()
        assert checkBoxPage.desktop_is_displayed() == True
        self.d_logger.info("Desktop menu is displayed")
         
    @pytest.mark.CheckBoxDocuments
    def test_documents_menu_present(self,driver_Setup):
        """Checks the Documents menu option is displayed"""
        self.driver = driver_Setup
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        check_Box_Page= CheckBoxPage(self.driver)
        mainp.click_elements_page()
        elements_page.click_check_box()
        check_Box_Page.click_expand_all()
        assert check_Box_Page.documents_is_displayed() is True
        self.d_logger.info("Documents menu is displayed")
        
    @pytest.mark.CheckboxChecked
    def test_checkbox_checked(self,driver_Setup):
        """Checks the check box is checked"""
        self.driver = driver_Setup
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        check_Box_Page= CheckBoxPage(self.driver)
        mainp.click_elements_page()
        elements_page.click_check_box_text()
        check_Box_Page.click_expand_all()
        check_Box_Page.click_check_box_home()
        checked,unchecked = check_Box_Page.home_is_checked()
        ch_string= checked[0]
        assert "home" in checked
        assert len(unchecked) == 0
        self.d_logger.info(f"Checked elements : {checked}")
     
    @pytest.mark.CheckBoxCheckedList
    def test_check_box_list(self,driver_Setup):
        """Checks the check box list is displayed"""
        self.driver = driver_Setup
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        check_Box_Page= CheckBoxPage(self.driver)
        mainp.click_elements_page()
        elements_page.click_check_box_text()
        check_Box_Page.click_expand_all()
        check_Box_Page.click_check_box_home()
        checked_list = check_Box_Page.get_checkbox_list()
        assert len(checked_list) == 18
        self.d_logger.info(f"Checked list : {checked_list}")
    
       