#!/usr/bin/env python3
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from Pages.BasePage import BasePage

class MainPage(BasePage):
    """ Main page class for the application """
    
    def __init__(self, driver):
        super().__init__(driver)
        self.elements_link = (By.XPATH,"//h5[text()='Elements']")
        self.forms_link = (By.XPATH,"//h5[text()='Forms']")
        self.alerts_link = (By.XPATH,"//h5[text()='Alerts, Frame & Windows']")
        self.widgets_link = (By.XPATH,"//h5[text()='Widgets']")
        self.interactions_link = (By.XPATH,"//h5[text()='Interactions']")
        self.book_store_link = (By.XPATH,"//h5[text()='Book Store Application']")
        self.footer_element = (By.XPATH,"//footer")

    
    def click_elements_page(self):
        """ Click on the element """
        BasePage.click_element(self,element =self.elements_link)

    def click_forms_page(self):
        """ Click on the element """
        BasePage.click_element(self,element =self.forms_link)   

    def click_alerts_page(self):
        """ Click on the element """
        BasePage.click_element(self,element = self.alerts_link)     

    def click_widgets_page(self):
        """ Click on the element """
        BasePage.click_element(self,element = self.widgets_link)

    def click_interactions_page(self):
        """ Click on the element """
        BasePage.click_element(self,element = self.interactions_link)

    def click_bookstore_page(self):
        """ Click on the element """    
        BasePage.click_element(self,element = self.book_store_link)

    def scroll_to_footer(self):
        """ Scroll to the footers page """
        BasePage.scroll_to_element(self,element = self.footer_element)
      