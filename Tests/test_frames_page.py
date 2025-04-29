#!/usr/bin/env python3
import pytest
import selenium
from Pages.MainPage import MainPage
from Pages.Elements_Page import ElementsPage
from Pages.IframePage import IFramePage
from Pages.log_config import logger
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
        f_page.go_to_iframe(f_frame)
        assert "This is a sample page" in driver.page_source