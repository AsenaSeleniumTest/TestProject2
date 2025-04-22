#!/usr/bin/env python3
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class Web_Table_Page(BasePage):
    """Page for Web Table Page"""
    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.web_table_title = (By.XPATH,"//h1[text()='Web Tables']")
        self.table_header_elements = (By.XPATH,"//div[@class='rt-resizable-header-content']")
        self.table_data_elements = (By.XPATH,"//div[@class='rt-td']")
        self.add_button = (By.XPATH,"//button[@id='addNewRecordButton']")
        self.form_title = (By.XPATH,"//div[text()='Registration Form']")
        self.form_first_name = (By.XPATH,"//input[@id='firstName']")
        self.form_last_name = (By.XPATH,"//input[@id='lastName']")
        self.form_email = (By.XPATH,"//input[@id='userEmail']")
        self.form_age= (By.XPATH,"//input[@id='age']")
        self.form_salary = (By.XPATH,"//input[@id='salary']")
        self.form_department = (By.XPATH,"//input[@id='department']")
        self.form_button_submit = (By.XPATH,"//button[@id='submit']")
        
        
    def get_header_elements(self):
        """ Get the header elements """
        return BasePage.get_element_list(self,elements = self.table_header_elements)
    def get_data_elements(self):
        """ Get the data elements """
        return BasePage.get_element_list(self,elements = self.table_data_elements)
    
    def click_add_button(self):
        """ Click the add button """        
        BasePage.click_element(self,element = self.add_button)
    
    def get_registration_form_title(self):
        """ Get the registered user """
        return BasePage.get_element(self,element = self.web_table_title)
    
    def add_first_name(self,first_name):
        """ Add first name """
        BasePage.type_text(self,element = self.form_first_name,text = first_name)
    
    def add_last_name(self,last_name):
        """ Add last name """
        BasePage.type_text(self,element = self.form_last_name,text = last_name)
    
    def add_email(self,email):
        """ Add email """
        BasePage.type_text(self,element = self.form_email,text = email)
        
    def add_age(self,age):
        """ Add age """
        BasePage.type_text(self,element = self.form_age,text = age)
        
    def add_salary(self,salary):
        """ Add salary """
        BasePage.type_text(self,element = self.form_salary,text = salary)
        
    def add_department(self,department):
        """ Add department """  
        BasePage.type_text(self,element = self.form_department,text = department)
    
    def click_submit_form(self):
        """ Click the submit button """
        BasePage.click_element(self,element = self.form_button_submit)