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
