#!/usr/bin/env python3
import pytest
from Pages.MainPage import MainPage
from Pages.Elements_Page import ElementsPage
from Pages.CheckBoxPage import CheckBoxPage
from Configuration.TestData import TestData

@pytest.mark.usefixtures("driver_Setup")
class Test_ElementsPage():
    """Test Elements page elements"""
    
        
    @pytest.mark.ElementsTitle
    def test_elementstitle(self,driver_Setup):
        """Test Page elements title is correct"""
        driver = driver_Setup
        driver.get(TestData.url)
        mainp = MainPage(driver)
        mainp.click_elements_page()
        #mainp.scroll_to_footer()
        assert driver.title == "DEMOQA"
        
    @pytest.mark.ElementsMenu
    def test_elementsmenu_count(self,driver_Setup):
        """Test Elements page elements"""     
        driver = driver_Setup
        driver.get(TestData.url)
        mainp = MainPage(driver)
        elements_page = ElementsPage(driver)
        mainp.click_elements_page()
        list_menu = elements_page.get_menu_list_elements()
        assert len(list_menu) == 9
        

    @pytest.mark.ElementsMenu 
    def test_click_text_box(self,driver_Setup):   
        """Test Elements page elements"""     
        driver = driver_Setup
        mainp = MainPage(driver)
        elements_page = ElementsPage(driver)
        mainp.click_elements_page()
        elements_page.click_check_box_text()
        

    @pytest.mark.TextBoxArea
    def test_text_box_form(self,driver_Setup):
        """Test text box form for Text box fields"""
        driver = driver_Setup
        driver.get(TestData.url)
        mainp = MainPage(driver)
        elements_page = ElementsPage(driver)
        mainp.click_elements_page()
        elements_page.click_text_box()
        elements_page.type_full_name(TestData.full_name)
        elements_page.type_email(TestData.email)
        elements_page.type_current_address(TestData.current_address)
        elements_page.type_permanent_address(TestData.Permanent_address)
        elements_page.click_submit_form()
        assert TestData.full_name in elements_page.get_submitted_name().text
    
    @pytest.mark.checkBoxTitle
    def test_check_box_forms(self,driver_Setup):
        """Test check box form for Text box fields"""
        driver = driver_Setup 
        driver.get(TestData.url)
        mainp = MainPage(driver)
        elements_page = ElementsPage(driver)
        checkBoxPage= CheckBoxPage(driver)
        mainp.click_elements_page()
        elements_page.click_check_box_text()
        text = checkBoxPage.get_check_box_title().text
        
        assert text == "Check Box"
    
    @pytest.mark.check
    def test_home_checked(self,driver_Setup):
        """Test check box form for Text box fields"""
        driver = driver_Setup 
        driver.get(TestData.url)
        mainp = MainPage(driver)
        elements_page = ElementsPage(driver)
        checkBoxPage= CheckBoxPage(driver)
        mainp.click_elements_page()
        elements_page.click_check_box_text()
        checkBoxPage.click_expand_all()
        checkBoxPage.click_check_box_home()
        elem_list_checked, elem_list_unchecked =checkBoxPage.home_is_checked()
        assert  len(elem_list_checked) == 17
        assert len(elem_list_unchecked) == 0
    
    
        