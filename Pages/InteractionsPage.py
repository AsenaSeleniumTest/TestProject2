#!/usr/bin/env python3
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class InteractionsPage(BasePage):
    """Interactions page class for the application"""
    
    def __init__(self, driver):
        """Initialize the Interactions page"""
        BasePage.__init__(self,driver)
        self.action = ActionChains(self.driver)
        self.sortable_menu = (By.XPATH,"//span[text()='Sortable']")
        self.selectable_menu = (By.XPATH,"//span[text()='Selectable']")
        self.resizable_menu = (By.XPATH,"//span[text()='Resizable']")
        self.droppable_menu = (By.XPATH,"//span[text()='Droppable']")
        self.dragabble_menu = (By.XPATH,"//span[text()='Dragabble']")
        #Headers
        self.sortable_header = (By.XPATH,"//h1[text()='Sortable']")
        self.one_element = (By.XPATH,"//div[text()='One']")
        self.two_element = (By.XPATH,"//div[text()='Two']")
        self.three_element = (By.XPATH,"//div[text()='Three']")
        self.sortable_list_elem = (By.XPATH,"//div[@id='sortableContainer']//div[contains(@class,'action')]")
        
    def click_sortable_menu(self):
        """Click on the Sortable menu"""
        self.click_element(self.sortable_menu)
    def click_selectable_menu(self):
        """Click on the Selectable menu"""
        self.click_element( self.selectable_menu)
    def click_resizable_menu(self):
        """Click on the Resizable menu"""
        self.click_element(self.resizable_menu)
    def click_droppable_menu(self):
        """Click to display dropabble elements """
        self.click_element(self.droppable_menu)
    def click_dragabble_menu(self):
        """click to display dragabble elements """
        self.click_element(self.dragabble_menu)
    
    def get_sortable_header(self):
        """Get the Sortable header"""
        return self.get_element(self.sortable_header)
    def move_mouse(self):
        """Move the mouse to the element"""
        self.action.move_to_element(self.sortable_header).perform()
        
    def drag_one_to_three(self):
        """Drag the One element to the Three element"""
        one = self.get_element(self.one_element)
        three = self.get_element(self.three_element)
        self.action.click_and_hold(one).move_to_element(three).release().perform()
    
    def get_sortable_list(self):
        """Split the list from grid"""
        sortable_elements = self.get_element_list2(self.sortable_list_elem)
        sortable_list = sortable_elements[0:6]
        return sortable_list
    
    def get_sortable_grid(self):
        """get sortablegri elements"""
        sortable_elements = self.get_element_list(self.sortable_list_elem)
        sortable_grid = sortable_elements[6:]
        return sortable_grid