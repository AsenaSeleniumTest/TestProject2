#!/usr/bin/env python3
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage
from Pages.Elements_Page import ElementsPage
from Pages.IframePage import IFramePage
from Pages.WidgetPage import WidgetPage
from Pages.InteractionsPage import InteractionsPage
from Pages.BookStorePage import BookStorePage

class MainPage(BasePage):
    """ Main page class for the application """
    
    def __init__(self, driver):
        BasePage.__init__(self,driver)
        self.elements_link = (By.XPATH,"//h5[text()='Elements']")
        self.forms_link = (By.XPATH,"//h5[text()='Forms']")
        self.alerts_link = (By.XPATH,"//h5[text()='Alerts, Frame & Windows']")
        self.widgets_link = (By.XPATH,"//h5[text()='Widgets']")
        self.interactions_link = (By.XPATH,"//h5[text()='Interactions']")
        self.book_store_link = (By.XPATH,"//h5[text()='Book Store Application']")
        self.footer_element = (By.XPATH,"//div[text()='Book Store Application']")

    
    def click_elements_page(self):
        """ Click on the element """
        self.click_element(self.elements_link)
        return ElementsPage(self.driver)

    def click_forms_page(self):
        """ Click on the element """
        self.click_element(self.forms_link)
        return ElementsPage(self.driver)

    def click_alerts_page(self):
        """ Click on the element """
        self.click_element(self.alerts_link)
        return IFramePage(self.driver)

    def click_widgets_page(self):
        """ Click on the element """
        self.click_element(self.widgets_link)
        return WidgetPage(self.driver)

    def click_interactions_page(self):
        """ Click on the element """
        self.click_element(self.interactions_link)
        return InteractionsPage(self.driver)

    def click_bookstore_page(self):
        """ Click on the element """    
        self.click_element(self.book_store_link)
        return BookStorePage(self.driver)

    
      