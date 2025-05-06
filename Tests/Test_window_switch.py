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
        
    @pytest.mark.RahulShettyAcademyTest
    def test_academy_new_tab(self, driver_Setup):
        """Test to validate the new tab from Rahul Shetty Academy"""
        driver = driver_Setup
        driver.get("https://rahulshettyacademy.com/")
        mainp=MainPage(driver)
        mainp.action.move_to_element(mainp.get_element((By.XPATH,"//a[text()='More ']"))).perform()
        mainp.action.move_to_element(mainp.get_element((By.XPATH,"//a[text()='Contact']"))).click(mainp.get_element((By.XPATH,"//a[text()='Contact']"))).perform()
        contact_mail = mainp.get_element((By.XPATH,"//h4[text()='E-mail']/parent::li"))
        driver.navigate().back()
        mainp.click_element((By.XPATH,"//a[text()='Login']"))
        mainp.get_element((By.XPATH,"//input[@id='email']")).send_keys(contact_mail.text)
        mainp.click_element((By.XPATH,"//span[text()='Log In']"))
        assert "Verify" == mainp.get_element((By.XPATH,"//span[text()='Verify']")).text
        
        
        
        
        
        
    