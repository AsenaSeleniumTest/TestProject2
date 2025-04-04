#!/usr/bin/env python3
import selenium.webdriver as webdriver
import logging as Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

from log_config import logger

class BasePage:
    
    

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)
        
    
    def get_title(self): 
        """ Get the title of the page """
        return self.driver.title

    def get_current_window(self):
        """ Get the current window handle """
        return self.driver.current_window_handle
    
    def click_element(self,element):
        try:
            logger.debug("clicking on element ",element )
            self.wait.until(EC.visibility_of_element_located(element)).click()
        except ElementClickInterceptedException as ex:
            logger.error("Error clicking element ", ex.__str__)
            print("Element is not clickable : ",ex.__str__)

    def element_status_displayed(self,element):
        """check if element is displayed"""
        try:
            logger.debug("Element displayed: ",element )
            return self.wait.until(EC.visibility_of_element_located(element)).is_displayed()
        except NoSuchElementException as ex:
            logger.error("Error  element not displayed  ", ex.__str__)
            print("element not found or took to much time to load : ",ex.__str__)                

    def type_text(self,element,text):
        try:
            self.wait.until(EC.visibility_of_element_located(element)).send_keys(text)
            logger.debug("Element keys sent : ",element )
        except ElementNotInteractableException as ex:  
            logger.error("Error  element not available for kye send    ", ex.__str__)
            print("Element cannot type data or is hidden : ", ex.__str__)       

    def get_element_list(self,elements):
        """ Get the list of elements on the webpage"""
        try:
            logger.debug("Getting element list : ",elements )
            return self.wait.until(EC.visibility_of_all_elements_located(elements))
        except NoSuchElementException as ex:
            logger.error("Error  element list not found  ", ex.__str__)
            return None

    def scroll_to_element(self,element):
        """ Scroll to the element """
        try:
            logger.debug("Scrolling to element : ",element )
            self.wait.until(EC.visibility_of_element_located(element))
            self.action.move_to_element(self.driver.find_element(element)).perform()
            #self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except NoSuchElementException as ex:
            logger.error("Error  element not found for scroll  ", ex.__str__)
            print("Element not found or took to much time to load : ",ex.__str__)    