#!/usr/bin/env python3
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage

class ElementsPage(BasePage):
    """ Elements page class for the application """
    menu_list_elements = (By.XPATH,"//div[@class='element-list collapse show']//li//span[@class='text']")
    textbox_name_element = (By.ID,"userName")
    textbox_mail_element = (By.ID,"userEmail")
    textbox_current_address_element = (By.ID,"currentAddress")
    textbox_permanent_address_element = (By.ID,"permanentAddress")
    textbox_submit_button_element = (By.ID,"submit")    




    def __init__(self, driver):
        super().__init__(driver)


    def get_menu_list_elements(self):
        """ Get the list of elements on the webpage"""
        return BasePage.get_element_list(self,elements = self.menu_list_elements)    

    def click_text_box(self):
        """ Click on the text box """
        for element in self.menu_list_elements:
            if element.text == "Text Box":
                BasePage.click_element(self,element = element)
                break  

    def type_full_name(self,text):
        """ Type the full name """
        BasePage.type_text(self,element = self.textbox_name_element,text = text)

    def click_check_box(self):
        """ Click on the check box """
        for element in self.menu_list_elements:
            if element.text == "Check Box":
                BasePage.click_element(self,element = element)
                break      

    def click_radio_button(self):    
        """ Click on the radio button """
        for element in self.menu_list_elements:
            if element.text == "Radio Button":
                BasePage.click_element(self,element = element)
                break    

    def click_web_tables(self):  
        """ Click on the web tables """
        for element in self.menu_list_elements:
            if element.text == "Web Tables":
                BasePage.click_element(self,element = element)
                break      