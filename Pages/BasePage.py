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
    
    def accept_alert(self):
        """method to accept alerts on the webpages"""
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoSuchElementException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/alert.png"
            self.driver.save_screenshot(screenshot_path)
            print("Alert not found or took too much time to load : ",ex)
            
    def accept_confirm_alert(self):
        """Method to accept confirm alerts on the webpages"""
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        except NoSuchElementException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/alert.png"
            self.driver.save_screenshot(screenshot_path)
            print("Alert not found or took too much time to load : ",ex)
            return ex
    
    def accept_prompt_alert(self,text):
        """Method to accept prompt alerts on the webpages"""
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        texto = alert.text
        alert.accept()
        return texto
    
    def click_element(self,element):
        """Method to click elements on the webpage"""
        try:
            self.wait.until(EC.visibility_of_element_located(element)).click()
        except ElementClickInterceptedException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/{element[1]}.png"
            self.driver.save_screenshot(screenshot_path)
            print("Element is not clickable : ",ex.__str__)

    def element_status_displayed(self,element):
        """check if element is displayed"""
        try:           
            return self.wait.until(EC.visibility_of_element_located(element)).is_displayed()
        except NoSuchElementException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/{element}.png"
            self.driver.save_screenshot(screenshot_path)           
            print("element not found or took to much time to load : ",ex.__str__)                

    def type_text(self,element,text):
        """Method to typetext on elements webpage"""
        try:
            self.wait.until(EC.visibility_of_element_located(element)).send_keys(text)        
        except ElementNotInteractableException as ex:  
            screenshot_path = f"error_screenshots/{self.timestamp}/{element}.png"
            self.driver.save_screenshot(screenshot_path)
            print("Element cannot type data or is hidden : ", ex.__str__)

    def get_element_list(self,elements):
        """ Get the list of elements on the webpage by visibility"""
        try:
            return self.wait.until(EC.visibility_of_all_elements_located(elements))
        except NoSuchElementException as ex:
            screenshot_path = f"./error_screenshots/{self.timestamp}/{elements}.png"
            self.driver.save_screenshot(screenshot_path)
            return ex
    def get_element_list2(self,elements):
        """get the elemenst by availability"""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(elements))
        except NoSuchElementException as ex:
            return ex
        
    def get_element(self,element):
        """ Get the text of the element """
        try:
            return self.wait.until(EC.visibility_of_element_located(element))
        except NoSuchElementException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/{element}.png"
            self.driver.save_screenshot(screenshot_path)
            return ex
       
    def scroll_to_element(self,element):
        """ Scroll to the element """ 
        try:
            self.wait.until(EC.presence_of_element_located(element))
            self.action.scroll_to_element(self.driver.find_element(element)).perform()
            #self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except NoSuchElementException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/{element}.png"
            self.driver.save_screenshot(screenshot_path)
            print("Element not found or took to much time to load : ",ex.__str__)
    
    
                 