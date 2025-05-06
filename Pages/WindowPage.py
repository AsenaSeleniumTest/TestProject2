#!/usr/bin/env python3
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class WindowsPage(BasePage):
    """Windows page class for the application"""
    
    def __init__(self, driver):
        """Initialize the Windows page"""
        BasePage.__init__(self,driver)
        self.new_tab_btn = (By.ID,"tabButton")
        self.new_window_btn = (By.ID,"windowButton")
        self.new_win_message_btn = (By.ID,"messageWindowButton")
        self.browser_window_menu = (By.XPATH,"//span[text()='Browser Windows']")
     
    def click_browser_window_menu(self):
        """Click on the Browser Window menu"""
        self.click_element(self.browser_window_menu)
        
    def click_new_tab_btn(self):
        """Click on the New Tab button"""
        self.click_element(self.new_tab_btn)
    
    def click_new_window_btn(self):
        """Click on the New Window button"""
        self.click_element(self.new_window_btn)
        
    def click_win_message_btn(self):
        """Click on the New Window Message button"""
        self.click_element(self.new_win_message_btn)
        
    def get_windows_in_session(self):
        """Get Window handles to switch to the new window"""
        return self.driver.window_handles
    
    