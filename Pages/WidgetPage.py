from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.SelectPage import SelectPage
class WidgetPage(BasePage):
    """Page clase for the Widget Menu"""
    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.select_menu_element = (By.XPATH,"//span[text()='Select Menu']")
        
        
    def click_select_menu(self):
        """function to click select menu"""
        self.driver.execute_script("window.scrollTo(0, 400);")
        self.click_element(self.select_menu_element)
        return SelectPage(self.driver)
    
    