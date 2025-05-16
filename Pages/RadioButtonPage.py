#!/usr/bin/env python3
import re
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class Radio_Button_Page(BasePage):
    """ Radio button page class for the application """
    
    def __init__(self, driver):
        BasePage.__init__(self,driver)
        self.driver = driver
        self.radio_button_title = (By.XPATH,"//h1[text()='Radio Button']")
        self.radio_button_yes = (By.XPATH,"//label[@for='yesRadio']")
        self.radio_button_impressive = (By.XPATH,"//label[@for='impressiveRadio']")
        self.radio_button_no = (By.XPATH,"//input[@id='noRadio']")
        self.radio_button_result = (By.XPATH,"//span[@class='text-success']")
        self.p_you_selected = (By.XPATH,"//p[@class='mt-3']")
        self.span_selected_yes = (By.XPATH,"//span[@class='text-success' and text()='Yes']")
        self.span_selected_impressive = (By.XPATH,"//span[@class='text-success' and text()='Impressive']")
        
    def get_radio_button_title(self):
        """ Get the radio button title """
        return self.get_element(self.radio_button_title)
    def click_radio_button_yes(self):
        """ Click on the radio button yes """
        self.click_element(self.radio_button_yes)
    def click_radio_button_impressive(self):
        """ Click on the radio button impressive """
        self.click_element(self.radio_button_impressive)    
    def radio_button_yes_is_displayed(self):
        """ Check if the radio button yes is displayed """
        return self.element_status_displayed(self.radio_button_yes)
    def radio_button_impressive_is_displayed(self):
        """ Check if the radio button impressive is displayed """
        return self.element_status_displayed(self.radio_button_impressive)
    def get_you_have_selected_label(self):
        """ Check if the you have selected text is displayed """
        return self.get_element(self.p_you_selected)
    def get_span_selected_yes(self):
        """ Get the span selected yes text """
        return self.get_element(self.span_selected_yes)
    def get_span_selected_impressive(self):
        """ Get the span selected impressive text """
        return self.get_element(self.span_selected_impressive)