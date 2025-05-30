#!/usr/bin/env python3
import pytest
from Pages.MainPage import MainPage
from Pages.Elements_Page import ElementsPage
from Pages.CheckBoxPage import CheckBoxPage
from Pages.log_config import logger
from Configuration.TestData import TestData

@pytest.mark.usefixtures("driver_Setup")
class Test_ElementsPage():
    """Test Elements page elements"""
    
        
    @pytest.mark.ElementsTitle
    def test_elementstitle(self,driver_Setup):  
        self.driver = driver_Setup
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        mainp.click_elements_page()
        #mainp.scroll_to_footer()
        logger.info("Browser opened ")
        assert self.driver.title == "DEMOQA"
         
        self.tear_down()

    @pytest.mark.ElementsMenu
    def test_elementsmenu_count(self,driver_Setup):    
        """Test Elements page elements"""     
        self.driver = driver_Setup
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        logger.info("Clicking on elements menu: %s", mainp.__class__)
        #mainp.scroll_to_footer()
        mainp.click_elements_page()
        list_menu = elements_page.get_menu_list_elements()
        assert len(list_menu) == 9
        

    @pytest.mark.ElementsMenu  
    def test_click_text_box(self,driver_Setup):   
        """Test Elements page elements"""     
        self.driver = driver_Setup
        mainp = MainPage(self.driver)
        elements_page = ElementsPage(self.driver)        
        mainp.click_elements_page()
        elements_page.click_check_box_text()
        

    @pytest.mark.TextBoxArea
    def test_text_box_form(self,driver_Setup):
        """Test text box form for Text box fields"""
        self.driver = driver_Setup 
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        mainp.click_elements_page()
        elements_page.click_text_box()
        elements_page.type_full_name(TestData.full_name)
        elements_page.type_email(TestData.email)
        elements_page.type_current_address(TestData.current_address)
        elements_page.type_permanent_address(TestData.Permanent_address)
        elements_page.click_submit_form()
        assert TestData.full_name == elements_page.get_submitted_name().text
    
    @pytest.mark.checkBoxTitle
    def test_check_box_forms(self,driver_Setup):
        """Test check box form for Text box fields"""
        self.driver = driver_Setup 
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        checkBoxPage= CheckBoxPage(self.driver)
        mainp.click_elements_page()
        elements_page.click_check_box_text()
        text = checkBoxPage.get_check_box_title().text
        
        assert text == "Check Box"    
    
    @pytest.mark.check
    def test_home_checked(self,driver_Setup):
        """Test check box form for Text box fields"""
        self.driver = driver_Setup 
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        checkBoxPage= CheckBoxPage(self.driver)
        mainp.click_elements_page()
        elements_page.click_check_box_text()
        checkBoxPage.click_expand_all()
        checkBoxPage.click_check_box_home()
        assert checkBoxPage.home_is_checked() is True
    
    def tear_down(self):
        """tear down the driver"""
        self.driver.quit()    
        