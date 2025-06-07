#!/usr/bin/env python3
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class SelectPage(BasePage):
    """Class PAge for select items"""
    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.div_input1_element=(By.XPATH,"//div[@id='withOptGroup']") #input elemente to click and type text
        self.input_element=(By.XPATH,"//div[@id='withOptGroup']//input")
        self.div_text_to_validate=(By.XPATH,"//div[@id='withOptGroup']/div/div/div")
        
    def click_select_value_dropdown(self,text):
        """method to click the input type select that is react """
        self.click_element(self.div_input1_element)
        self.type_text(self.input_element, text = text)
        self.action.key_down(Keys.ENTER).perform()
        return self.get_element(self.div_text_to_validate)