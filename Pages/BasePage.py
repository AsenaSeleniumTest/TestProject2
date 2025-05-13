#!/usr/bin/env python3
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from Configuration.log_config import *

class BasePage:
    """ Base page for Page Object Model"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)
        self.logger = get_debug_logger_()
        self.c_logger = get_critical_logger()
    
    def get_title(self):
        """ Get the title of the page """
        self.logger.debug("Getting the title of the page")
        return self.driver.title

    def get_current_window(self):
        """ Get the current window handle """
        self.logger.debug("Getting the current window handle %s",self.driver.current_window_handle)
        return self.driver.current_window_handle
    
    def accept_alert(self):
        """method to accept alerts on the webpages"""
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            texto = alert.text
            alert.accept()
            self.logger.debug("Alert accepted : %s",texto)
            return texto
        except NoSuchElementException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/alert.png"
            self.driver.save_screenshot(screenshot_path)
            self.c_logger.error("Alert not found or took too much time to load : %s ",ex)
            
    def accept_confirm_alert(self):
        """Method to accept confirm alerts on the webpages"""
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            self.logger.debug("Alert accepted : %s",text)
            return text
        except NoSuchElementException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/alert.png"
            self.driver.save_screenshot(screenshot_path)
            self.c_logger.error("Alert not found or took too much time to load : %s ",ex)
            return ex
    
    def accept_prompt_alert(self,text):
        """Method to accept prompt alerts on the webpages"""
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        texto = alert.text
        alert.accept()
        self.logger.debug("Alert accepted : %s",texto)
        return texto
    
    def cancel_alert(self):
        """Method to cance an alert on the webpage"""
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            self.logger.debug("Alert text dismissed : %s",alert.text)
            alert.dismiss()
        except NotImplementedError as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/alert.png"
            self.driver.save_screenshot(screenshot_path)
            self.c_logger.error("Alert not found or took too much time to load : %s",ex)
            return ex
        
    def click_element(self,element):
        """Method to click elements on the webpage"""
        try:
            self.wait.until(EC.visibility_of_element_located(element)).click()
            self.logger.debug("Element clicked : %s",element)
        except ElementClickInterceptedException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/{element}.png"
            self.driver.save_screenshot(screenshot_path)
            self.c_logger.error("Element is not clickable : %s",ex.__str__)

    def element_status_displayed(self,element):
        """check if element is displayed"""
        try:
            self.logger.debug("Checking if element is displayed : %s",element)
            return self.wait.until(EC.visibility_of_element_located(element)).is_displayed()
        except NoSuchElementException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/{element}.png"
            self.driver.save_screenshot(screenshot_path)           
            self.c_logger.error("element not found or took to much time to load : %s ",ex.__str__)

    def type_text(self,element,text):
        """Method to typetext on elements webpage"""
        try:
            self.wait.until(EC.visibility_of_element_located(element)).send_keys(text)
            self.logger.debug("Text typed : %s",text)
        except ElementNotInteractableException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/{element}.png"
            self.driver.save_screenshot(screenshot_path)
            self.c_logger.error("Element cannot type data or is hidden : %s ", ex.__str__)

    def get_element_list(self,elements):
        """ Get the list of elements on the webpage by visibility"""
        try:
            self.logger.debug("Getting the list of elements : %s",elements)
            return self.wait.until(EC.visibility_of_all_elements_located(elements))
        except NoSuchElementException as ex:
            screenshot_path = f"./error_screenshots/{self.timestamp}/{elements}.png"
            self.driver.save_screenshot(screenshot_path)
            self.c_logger.error("Elements not found or took too much time to load : %s ",ex.__str__)
            return ex
        
    def get_element_list2(self,elements):
        """get the elemenst by availability"""
        try:
            self.logger.debug("Getting the list of elements : %s",elements)
            return self.wait.until(EC.presence_of_all_elements_located(elements))
        except NoSuchElementException as ex:
            self.c_logger.error("Elements not found or took too much time to load : %s ",ex.__str__)
            return ex
        
    def get_element(self,element):
        """ Get the text of the element """
        try:
            self.logger.debug("Getting the element : %s",element)
            return self.wait.until(EC.visibility_of_element_located(element))
        except NoSuchElementException as ex:
            screenshot_path = f"error_screenshots/{self.timestamp}/{element}.png"
            self.driver.save_screenshot(screenshot_path)
            self.c_logger.error("Element not found or took too much time to load : %s ",ex.__str__)
            return ex
       
    