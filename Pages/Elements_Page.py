#!/usr/bin/env python3
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.Forms_Page import Forms_Page
from Pages.CheckBoxPage import CheckBoxPage
class ElementsPage(BasePage):
    """ Elements page class for the application """
        
    def __init__(self, driver):
        BasePage.__init__(self,driver)
        self.texbox_span = (By.XPATH,"//span[text()='Text Box']")
        self.submit_form = (By.XPATH,"//button[@id='submit']")
        self.menu_list_elements = (By.XPATH,"//div[@class='element-list collapse show']//li//span[@class='text']")
        self.textbox_name_element = (By.ID,"userName")
        self.textbox_mail_element = (By.ID,"userEmail")
        self.textbox_current_address_element = (By.ID,"currentAddress")
        self.textbox_permanent_address_element = (By.ID,"permanentAddress")
        self.textbox_submit_button_element = (By.ID,"submit")
        self.submit_name = (By.XPATH,"//p[@id='name']")
        self.submit_email = (By.XPATH,"//p[@id='email']")
        self.submit_current_address = (By.XPATH,"//p[@id='currentAddress']")
        self.submit_permanent_address = (By.XPATH,"//p[@id='permanentAddress  ']")
        """Check box elements"""
        self.check_box_span = (By.XPATH,"//span[text()='Check Box']")
        self.radio_button_span = (By.XPATH,"//span[text()='Radio Button']")
        self.web_tables_span = (By.XPATH,"//span[text()='Web Tables']")
        self.alert_frame_window = (By.XPATH,"//span[text()='Alerts, Frame & Windows']")
        self.practice_form_menu = (By.XPATH,"//span[text()='Practice Form']")
        
    def get_menu_list_elements(self):
        """ Get the list of elements on the webpage"""
        return self.get_element_list(self.menu_list_elements)

    def click_text_box(self):
        """ Click on the text box """
        elements = self.get_menu_list_elements()
        for element_a in elements:
            print(element_a.text)
            if element_a.text == "Text Box":
                self.click_element(self.texbox_span)
                break

    def type_full_name(self,text):
        """ Type the full name """
        self.type_text(self.textbox_name_element,text)
    
    def type_email(self,text):
        """ Type the email """
        self.type_text(self.textbox_mail_element,text)
    
    def type_current_address(self,text):
        """ Type the current address """  
        self.type_text(self.textbox_current_address_element,text)
    
    def type_permanent_address(self,text):
        """ Type the permanent address """
        self.type_text(self.textbox_permanent_address_element,text)

    def click_check_box(self):
        """ Click on the check box """
        for element in self.menu_list_elements:
            if self.get_element(element).text == "Check Box":
                self.click_element(element)
                break

    def click_practice_form_menu(self):
        """click on the practice form menu"""
        self.click_element(self.practice_form_menu)
        return Forms_Page(self.driver)
        
    def click_web_tables(self):  
        """ Click on the web tables """
        for element in self.menu_list_elements:
            if self.get_element(element).text == "Web Tables":
                self.click_element(element)
                break

    def get_submitted_name(self):
        """ Get the submitted name """
        return self.get_element(self.submit_name)

    def click_submit_form(self):
        """ Click on the submit form """
        self.click_element( self.submit_form)

    def click_check_box_text(self):
        """ Click on the check box """
        self.click_element(self.check_box_span)
        return CheckBoxPage(self.driver)
    
    def click_radio_button_menu(self):
        """ Click on the radio button """
        self.click_element(self.radio_button_span)
    
    def click_web_tables_menu(self):  
        """ Click on the web tables """
        self.click_element(self.web_tables_span)
    
    def click_alert_frame_window_menu(self):
        """click menu for Alert, Frame and windows"""
        self.click_element(self.alert_frame_window)