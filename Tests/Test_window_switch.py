#!/usr/bin/env python3
import pytest
from selenium.webdriver.common.by import By
from Pages.MainPage import MainPage
from Pages.WindowPage import WindowsPage
from Configuration.TestData import TestData


@pytest.mark.usefixtures("driver_Setup")
class Test_window_page():
    """Class to test window page"""
    
    @pytest.mark.window
    def test_window(self, driver_Setup):
        """Test to validate the window page"""
        driver = driver_Setup
        driver.get(TestData.url)
        mainp = MainPage(driver)
        w_page = WindowsPage(driver)
        mainp.click_alerts_page()
        assert "Dragabble" in driver.page_source
        
    @pytest.mark.new_tab
    def test_new_tab(self, driver_Setup):
        """Test to validate the new tab"""
        driver = driver_Setup
        driver.get(TestData.url)
        mainp = MainPage(driver)
        w_page = WindowsPage(driver)
        mainp.click_alerts_page()
        w_page.click_browser_window_menu()
        w_page.click_new_tab_btn()
        whandles = w_page.get_windows_in_session()
        driver.switch_to.window(whandles[1])
        new_page_element = w_page.get_element((By.ID,"sampleHeading"))
        assert new_page_element.text == "This is a sample page"
        assert len(whandles) == 2   