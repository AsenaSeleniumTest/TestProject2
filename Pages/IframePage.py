from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class IFramePage(BasePage):
    """Class to handel iframes """
    def __init__(self, driver):
        BasePage.__init__(self,driver)
        self.frame_list = (By.XPATH,"//iframe")
        #HS28291115
    
    def get_frame_list(self):
        """get all frame list"""
        return BasePage.get_element_list(self, elements = self.frame_list)
    
    def find_iframe(self,text):
        """function to switch to the element frame"""
        for nframe in self.get_frame_list():
            self.driver.switch_to().frame(nframe)
            if text in self.driver.page_source:
                return nframe
            else:
                return None