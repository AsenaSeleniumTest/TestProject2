from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException

class IFramePage(BasePage):
    """Class to handel iframes """
    def __init__(self, driver):
        BasePage.__init__(self,driver)
        self.frame_menu = (By.XPATH,"//span[text()='Frames']")
        self.frame1 = (By.XPATH,"//div//iframe[@id='frame1']")
        self.frame_list = (By.XPATH,"//div//iframe")
        #HS28291115
    
    def get_frame_list(self):
        """get all frame list"""
        return BasePage.get_element_list(self, elements = self.frame_list)
    
    def get_frame(self,text):
        """get frame"""
        return BasePage.get_element(self, element = (By.XPATH,f"//iframe[@id='{text}']"))
        
    def go_to_iframe(self,frame):
        """function to switch to the element frame"""
        try:
            self.driver.switch_to.frame(frame)
        except NoSuchElementException as ex:
            print("Element not found or took too much time to load : ",ex)
            return ex
        except Exception as ex:
            print("Error switching to frame : ",ex)
            return ex
        
    def click_frame_menu(self):
        """click frame from left menu"""
        BasePage.click_element(self, element = self.frame_menu)
                