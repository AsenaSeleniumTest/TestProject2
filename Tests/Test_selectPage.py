#!/usr/bin/env python3
import pytest
from Pages.MainPage import MainPage
from Pages.WidgetPage import WidgetPage
from Pages.SelectPage import SelectPage
from Configuration.TestData import TestData


@pytest.mark.usefixtures("driver_Setup")
class Test_Select_Page():
    """test clase for select type elements"""
    
    @pytest.mark.testReactSelect
    def test_select_option_1(self,driver_Setup):
        """Test case to validate the option selected is correct"""
        driver = driver_Setup
        driver.get(TestData.url)
        mainp = MainPage(driver)
        wPage = WidgetPage(driver)
        sPage = SelectPage(driver)
        mainp.click_widgets_page()
        wPage.click_select_menu()
        sPage.click_select_value_dropdown()
        sPage.type_text_select_dropdown("Group 2, option 1")
        expected_element = sPage.get_element_selected()
        assert "Group 2, option 1" == expected_element.text
        
        
        
        
        
        