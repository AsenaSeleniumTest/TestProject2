import re
import pytest
from log_config import logger
from Pages.MainPage import MainPage
from Pages.Elements_Page import ElementsPage
from Pages.CheckBoxPage import CheckBoxPage
from Configuration.TestData import TestData


@pytest.mark.usefixtures("driver_Setup")
class Test_CheckBoxPage():
    """Test Check Box page elements"""
    driver = None

    @pytest.mark.CheckBoxTitle
    def test_checkboxtitle(self,driver_Setup):    
        """Checks the Check Box title is displayed"""
        self.driver = driver_Setup 
        self.driver.get(TestData.url) 
        mainp =MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        checkBoxPage= CheckBoxPage(self.driver)
        mainp.click_elements_page()
        elements_page.click_check_box()
        checkBoxPage.click_expand_all()
        texto = checkBoxPage.get_check_box_title().text
        logger.info(f"Check Box title is {texto}")
        assert texto == "Check Box"
        

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
        assert len(unchecked) is 0
     
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
    
       