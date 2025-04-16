#!/usr/bin/env python3
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from Tests.log_config import logger

class BasePage:
    """ Base page for Page Object Model"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    

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
            logger.debug(f"clicking on element: {element}" )
            self.wait.until(EC.visibility_of_element_located(element)).click()
        except ElementClickInterceptedException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/{element[1]}.png"
            self.driver.save_screenshot(screenshot_path)
            logger.error(f"Error clicking element: {ex.__str__} ")
            print("Element is not clickable : ",ex.__str__)

    def element_status_displayed(self,element):
        """check if element is displayed"""
        try:
            logger.debug(f"Element displayed: {element} ")
            return self.wait.until(EC.visibility_of_element_located(element)).is_displayed()
        except NoSuchElementException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/{element}.png"
            self.driver.save_screenshot(screenshot_path)
            logger.error(f"Error  element not displayed :  {ex.__str__}")
            print("element not found or took to much time to load : ",ex.__str__)                

    def type_text(self,element,text):
        try:
            self.wait.until(EC.visibility_of_element_located(element)).send_keys(text)
            logger.debug(f"Element keys sent : {element}" )
        except ElementNotInteractableException as ex:  
            screenshot_path = f"error_screenshots/{self.timestamp}/{element}.png"
            self.driver.save_screenshot(screenshot_path)
            logger.error(f"Error  element not available for key send : {ex.__str__} ")
            print("Element cannot type data or is hidden : ", ex.__str__)       

    def get_element_list(self,elements):
        """ Get the list of elements on the webpage"""
        try:
            logger.debug(f"Getting element list : {elements}" )
            return self.wait.until(EC.visibility_of_all_elements_located(elements))
        except NoSuchElementException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/{elements}.png"
            self.driver.save_screenshot(screenshot_path)
            logger.error(f"Error  element list not found : {ex.__str__}")
            return None

    def get_element(self,element):
        """ Get the text of the element """
        try:
            logger.debug(f"Getting element text : {element} ")
            return self.wait.until(EC.visibility_of_element_located(element))
        except NoSuchElementException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/{element}.png"
            self.driver.save_screenshot(screenshot_path)
            logger.error(f"Error  element not found for text: {ex.__str__} ")
            return None
        
    def scroll_to_element(self,element):
        """ Scroll to the element """ 
        try:
            logger.debug(f"Scrolling to element : {element} ")
            self.wait.until(EC.visibility_of_element_located(element))
            self.action.move_to_element(self.driver.find_element(element)).perform()
            #self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except NoSuchElementException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/{element}.png"
            self.driver.save_screenshot(screenshot_path)
            logger.error(f"Error  element not found for scroll : {ex.__str__} ")
            print("Element not found or took to much time to load : ",ex.__str__)
    
    
                 