
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class BookStorePage(BasePage):
    """Class for Book store Page Actions"""
    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.__login_menu_button = (By.XPATH,"//span[text()='Login']")
        self.__user_namme_input = (By.XPATH,"//input[@id='userName']")
        self.__password_input = (By.ID,"password")
        self.__login_button = (By.ID,"login")
        self.__new_user_button = (By.ID,"newUser")
        self.__new_first_name_input = (By.ID,"firstname")
        self.__new_last_name_input = (By.ID,"lastname")
        self.__new_username_input = (By.ID,"userName")
        self.__new_password_input = (By.ID,"password")
        self.__captcha_frame = (By.XPATH,"//iframe[@title='reCAPTCHA']")
        self.__captcha_input = (By.XPATH,"//span[@id='recaptcha-anchor']")
        self.__register_button = (By.ID,"register")
        self.__invalid_user_message = (By.XPATH,"//p[@id='name']")
        #Menu button for book store
        self.__book_store_menu_button = (By.XPATH,"//span[text()='Book Store']")
        self.__profile_menu_button = (By.XPATH,"//span[text()='Profile']")
        self.__book_store_api_menu_button = (By.XPATH,"//span[text()='Book Store API']")
            
    def login_function_invalid(self,username, password):
        """method to test login to book store application"""
        self.click_element(self.__login_menu_button)
        self.type_text(self.__user_namme_input, username)
        self.type_text(self.__password_input, password)
        self.click_element(self.__login_button)
        return self.get_element(self.__invalid_user_message)
    
    def login_function(self,username, password):
        """method to test login to book store application"""
        self.click_element(self.__login_menu_button)
        self.type_text(self.__user_namme_input, username)
        self.type_text(self.__password_input, password)
        self.click_element(self.__login_button)
          
     
    def create_user(self,fName, lName, userName, password):
        """Method to create a new user in book store application"""
        self.click_element(self.__new_user_button)
        self.type_text(self.__new_first_name_input, fName)
        self.type_text(self.__new_last_name_input, lName)
        self.type_text(self.__new_username_input, userName)
        self.type_text(self.__new_password_input,password)
        self.driver.switch_to.frame(self.get_element(self.__captcha_frame))
        self.click_element(self.__captcha_input)
        self.click_element(self.__register_button)
        message = self.accept_alert()
        return message
        