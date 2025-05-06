from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Pages.BasePage import BasePage


class IFramePage(BasePage):
    """Class to handel iframes """
    def __init__(self, driver):
        BasePage.__init__(self,driver)
        self.frame_menu = (By.XPATH,"//span[text()='Frames']")
        self.frame1 = (By.XPATH,"//div//iframe[@id='frame1']")
        self.frame_list = (By.XPATH,"//div//iframe")
        self.alerts_page =(By.XPATH,"//span[text()='Alerts']")
        self.alert_button1 = (By.XPATH,"//button[@id='alertButton']")
        self.timer_alert_button = (By.XPATH,"//button[@id='timerAlertButton']")
        self.confirm_alert_button = (By.XPATH,"//button[@id='confirmButton']")
        self.prompt_alert_button = (By.XPATH,"//button[@id='promtButton']")
        self.confirm_alert_emessage = (By.XPATH,"//span[@id='confirmResult']")
        self.prompt_alert_emessage = (By.XPATH,"//span[@id='promptResult']")
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
    
    def click_alerts_menu(self):
        """click alerts page from left menu"""
        BasePage.click_element(self, element = self.alerts_page)
    
    def click_alert_button1(self):
        """click alert button"""
        BasePage.click_element(self, element = self.alert_button1)
    
    def click_alert_button2(self):
        """click alert button"""
        BasePage.click_element(self, element = self.timer_alert_button)
    
    def click_alert_button3(self):
        """click alert button"""
        BasePage.click_element(self, element = self.confirm_alert_button)
        
    def click_alert_button4(self):
        """click alert button"""
        BasePage.click_element(self, element = self.prompt_alert_button)
    def dismiss_alert(self):
        """function to dismiss alert"""
        BasePage.cancel_alert(self)
    def alert_dismiss_message(self):
        """function to get alert message"""
        return BasePage.get_element(self, element = self.confirm_alert_emessage)