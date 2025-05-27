#!/usr/bin/env python3
import re
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from Pages.BasePage import BasePage

class CheckBoxPage(BasePage):
    """ Check box page class for the application """
    
    def __init__(self, driver):
        BasePage.__init__(self,driver)
        self.expand_all_button = (By.XPATH,"//button[@title='Expand all']")
        self.collapse_all_button = (By.XPATH,"//button[@title='Collapse all']")
        self.check_box_title = (By.XPATH,"//h1[text()='Check Box']")
        self.check_box_all_expanded= (By.XPATH,"//span[@class='rct-text']//button")
        self.check_box_home = (By.XPATH,"//span[text()='Home']/ancestor::label")
        self.expand_destktop = (By.XPATH,"")
        self.check_box_desktop = (By.XPATH,"//span[text()='Desktop']")
        self.check_box_documents= (By.XPATH,"//span[text()='Documents']")
        self.check_box_downloads = (By.XPATH,"//div[@id='result']//span[@class='text-success']")
        self.check_box_check = (By.XPATH,"//*[name()='svg' and @class='rct-icon rct-icon-check']")
        self.check_box_unchecked = (By.XPATH,"//*[name()='svg' and @class='rct-icon rct-icon-uncheck']")
        self.text_checked_elements = (By.XPATH,"//div[@id='result']/span")
        self.checkbox_list = (By.CSS_SELECTOR,"input[type='checkbox']")
        
    def get_check_box_title(self):
        """ Get the check box title """
        return self.get_element(self.check_box_title)

    def click_expand_all(self):
        """ Click on the expand all checkboxes must be count of 6 """
        self.click_element(self.expand_all_button)
        return self.get_element_list(self.check_box_all_expanded)
        
    def click_collapse_all(self):
        """Method to test collapse all checkbox list must return count of 1"""
        self.click_element(self.expand_all_button)
        self.click_element(self.collapse_all_button)
        return self.get_element_list(self.check_box_all_expanded)
    
#pendiente continuar desde aqui para los nuevos metodos, refactorizados
    def desktop_is_displayed(self):
        """ Check if the desktop is displayed """
        return self.element_status_displayed(self.check_box_desktop)
    
    def documents_is_displayed(self):
        """ Check if the documents is displayed """
        return self.element_status_displayed(self.check_box_documents)
    
    def click_check_box_home(self):
        """ Click on the check box home """
        self.click_element(self.check_box_home)
        
    def home_is_checked(self):
        """ Check if the home is checked """
        items_checked = []
        items_unchecked = []
        if self.element_status_displayed(self.check_box_home) is True:
            elem = self.get_element_list2(self.checkbox_list)
            print("elements : ",elem)
            for el in elem:
                if el.is_selected():
                    items_checked.append(el.get_property("id"))
                else:
                    items_unchecked.append(el.get_property("className"))
            return items_checked, items_unchecked
        else:
            raise ElementNotVisibleException(f"Element not found : {self.check_box_home}")
    
    def get_checkbox_list(self):
        """ Get the check box list """
        return self.get_element_list(self.text_checked_elements)
    
             