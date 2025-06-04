#!/usr/bin/env python3
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class SelectPage(BasePage):
    """Class PAge for select items"""
    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.div_input1_element=(By.XPATH,"//div[@id='withOptGroup']") #input elemente to click and type text
        self.input_element=(By.XPATH,"//div[@id='withOptGroup']//input")
        self.div_text_to_validate=(By.XPATH,"//div[@id='withOptGroup']/div/div/div")
        
    def click_select_value_dropdown(self):
        """method to click the input type select that is react """
        BasePage.click_element(self, element = self.div_input1_element)
    
    def type_text_select_dropdown(self,text):
        """method to type the text to find item in the dropdown, empty if text input has not match value"""
        BasePage.type_text(self, element = self.input_element, text = text)
    
    def get_element_selected(self):
        """get the selected element exist on the dropdown options"""
        return BasePage.get_element(self, element = self.div_text_to_validate)
        
   