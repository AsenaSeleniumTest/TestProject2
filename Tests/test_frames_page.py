#!/usr/bin/env python3
import pytest
from Pages.MainPage import MainPage
from Pages.IframePage import IFramePage
from Configuration.TestData import TestData

@pytest.mark.usefixtures("driver_Setup")
class Test_frames_page():
    """Class to test frames """
    
    @pytest.mark.framecount
    def test_frame_switch(self,driver_Setup):
        """Test to validate the selected frame"""
        driver = driver_Setup
        driver.get(TestData.url)
        mainp = MainPage(driver)
        f_page = IFramePage(driver)
        mainp.click_alerts_page()
        f_page.click_frame_menu()
        f_frame = f_page.get_frame("frame1")
        print("Width: " + f_frame.get_property("width"))
        element = f_page.go_to_iframe(f_frame)
        assert "This is a sample page" == element.text
    
    @pytest.mark.frameswitch
    def test_frame2_switch(self, driver_Setup):
        """Test to validate the selected frame"""
        driver = driver_Setup
        driver.get(TestData.url)
        mainp = MainPage(driver)
        f_page = IFramePage(driver)
        mainp.click_alerts_page()
        f_page.click_frame_menu()
        f_frame = f_page.get_frame("frame2")        
        print("Width: " + f_frame.get_property("width"))
        element = f_page.go_to_iframe(f_frame)
        assert "This is a sample page" == element.text
    
    @pytest.mark.testalert
    def test_alert(self,driver_Setup):
        """Test alert accept"""
        driver = driver_Setup
        driver.get(TestData.url)
        mainp = MainPage(driver)
        f_page = IFramePage(driver)
        mainp.click_alerts_page()
        f_page.click_alerts_menu()
        f_page.click_alert_button1()
        alert_text = f_page.accept_alert()
        assert alert_text == "You clicked a button"
    
    @pytest.mark.testTimerAlert
    def test_timer_alert(self,driver_Setup):
        """Test timer alert accept"""
        driver = driver_Setup
        driver.get(TestData.url)
        mainp = MainPage(driver)
        f_page = IFramePage(driver)
        mainp.click_alerts_page()
        f_page.click_alerts_menu()
        f_page.click_alert_button2()
        alert_text = f_page.accept_alert()
        assert alert_text == "This alert appeared after 5 seconds"
    
    @pytest.mark.testconfirmalert
    def test_confirm_alert(self,driver_Setup):
        """Test confirm alert accept"""
        driver = driver_Setup
        driver.get(TestData.url)
        mainp = MainPage(driver)
        f_page = IFramePage(driver)
        mainp.click_alerts_page()
        f_page.click_alerts_menu()
        f_page.click_alert_button3()
        alert_text = f_page.accept_confirm_alert()
        assert alert_text == "Do you confirm action?"
    @pytest.mark.testAlertDismiss
    def test_alert_dismiss(self,driver_Setup):
        """Test alert dismiss"""
        driver = driver_Setup
        driver.get(TestData.url)
        mainp = MainPage(driver)
        f_page = IFramePage(driver)
        mainp.click_alerts_page()
        f_page.click_alerts_menu()
        f_page.click_alert_button3()
        f_page.dismiss_alert()
        assert f_page.alert_dismiss_message().text == "You selected Cancel"
        
    @pytest.mark.testPromptalert
    def test_prompt_alert(self,driver_Setup):
        """Test prompt alert accept"""
        driver = driver_Setup
        driver.get(TestData.url)
        mainp = MainPage(driver)
        f_page = IFramePage(driver)
        mainp.click_alerts_page()
        f_page.click_alerts_menu()
        f_page.click_alert_button4()
        alert_text = f_page.accept_prompt_alert("Hello")
        assert alert_text == "Please enter your name"    