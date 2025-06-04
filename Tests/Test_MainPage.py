#!/usr/bin/env python3
import pytest
from Pages.BasePage import BasePage
from Pages.MainPage import MainPage
from Configuration.TestData import TestData

@pytest.mark.usefixtures("driver_Setup")
class Test_Main_Page():
    """Test Main page elements"""
    driver = None

    @pytest.mark.WelcomeTitle
    def test_welcometitle(self,driver_Setup):
        self.driver = driver_Setup 
        self.driver.get(TestData.url)
        bPage=BasePage(self.driver)
        mainp =MainPage(self.driver)
    
        
        assert self.driver.title == "DEMOQA"

    @pytest.mark.MenuList
    def test_menu_list(self,driver_Setup):
        expected = ['Elements', 'Forms', 'Alerts, Frame & Windows', 'Widgets', 'Interactions', 'Book Store Application']
        self.driver = driver_Setup
        self.driver.get(TestData.url)
        b_page = BasePage(self.driver)
        main_page = MainPage(self.driver)
        result = main_page.get_menu_list()
        for i,item in enumerate(result):
            assert expected[i] == item.text, f"Expected {expected}, but got {result}"
        