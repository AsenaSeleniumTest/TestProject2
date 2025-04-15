#!/usr/bin/env python3
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException


from Pages.BasePage import BasePage

class CheckBoxPage(BasePage):
    """ Check box page class for the application """
    
   

    def __init__(self, driver):
        super().__init__(driver)
        self.check_box_title = (By.XPATH,"//h1[text()='Check Box']")
        self.check_box_expand_all = (By.XPATH,"//span[@class='rct-text']//button")
        self.check_box_home = (By.XPATH,"//span[text()='Home']/ancestor::label")
        self.check_box_desktop = (By.XPATH,"//span[text()='Desktop']")
        self.check_box_documents= (By.XPATH,"//span[text()='Documents']")
        self.check_box_downloads = (By.XPATH,"//div[@id='result']//span[@class='text-success']")
        self.check_box_check_element = (By.XPATH,"//*[name()='svg' and @class='rct-icon rct-icon-uncheck']")

    def get_check_box_title(self):
        """ Get the check box title """
        return BasePage.get_element(self,element = self.check_box_title)

    def click_expand_all(self):
        """ Click on the expand all button """
        BasePage.click_element(self,element = self.check_box_expand_all)
    
    def desktop_is_displayed(self):
        """ Check if the desktop is displayed """
        return BasePage.element_status_displayed(self,element = self.check_box_desktop) 
    
    def documents_is_displayed(self):
        """ Check if the documents is displayed """
        return BasePage.element_status_displayed(self,element = self.check_box_documents)
    
    def click_check_box_home(self):
        """ Click on the check box home """
        BasePage.click_element(self,element = self.check_box_home)
        
    def home_is_checked(self):
        """ Check if the home is checked """
        items_checked = []
        items_unchecked = []
        if BasePage.element_status_displayed(self,element = self.check_box_home) == True:
            elem = BasePage.get_element_list(self,elements = self.check_box_check_element)
            for el in elem:
                clase = elem.get_attribute("class")
                if "rct-icon rct-icon-check" in clase:
                    items_checked.append(el.text)
                else:
                    items_unchecked.append(el.text)
            return items_checked, items_unchecked        
        else:
            raise ElementNotVisibleException(f"Element not found : {self.check_box_home}")   
        
             