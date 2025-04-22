from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class WidgetPage(BasePage):
    """Page clase for the Widget Menu"""
    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.select_menu_element = (By.XPATH,"//span[text()='Select Menu']")
        
        
    def click_select_menu(self):
        """function to click select menu"""
        BasePage.click_element(self,element = self.select_menu_element)
        