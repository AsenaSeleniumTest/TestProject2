from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class Forms_Page(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.__name = (By.XPATH,"//input[@id='firstName']")
        self.__last_name =(By.ID,"lastName")
        self.__email = (By.ID,"userEmail")
        self.__gender_radio_list = (By.NAME,"gender")
        self.__gender_label_list = (By.XPATH,"//input[@name='gender']//parent::div//label")
        self.__mobile = (By.ID,"userNumber")
        self.__dob = (By.ID,"dateOfBirthInput")
        self.__subjects = (By.ID,"subjectsInput")
        self.__hobbies = (By.XPATH,"//input[@type='checkbox']")
        self.__picture_file = (By.ID,"uploadPicture")
        self.__current_address = (By.ID,"currentAddress")
        self.__state = (By.XPATH,"//div[@id='state']//input")
        self.__city = (By.XPATH,"//div[@id='city']//input")
        self.__submit_button = (By.XPATH,"//button[@id='submit']")
        #elements for the modal on submit
        self.__title_submitted = (By.XPATH,"//div[text()='Thanks for submitting the form']")
        
    
    def fill_form(self,first_name,lname,email,gender,mnumber,dob,subject,cbox,path,address,state,city):
        """Method to fill the form with the given data"""
        self.type_user_name(first_name)
        self.type_last_name(lname)
        self.type_email(email)
        self.select_gender(gender)
        self.type_mobile(mnumber)
        self.type_date_of_birth(dob)
        self.type_subjects(subject)
        self.select_hobbies(cbox)
        self.upload_file(path)
        self.type_current_address(address)
        self.select_state(state)
        self.select_city(city)
        self.click_submit_form()
        return self.get_submitted_form_title()
        
    def type_user_name(self,first_name):
        """Type the user name"""
        self.type_text(self.__name,first_name)
            
    def type_last_name(self,lname):
        """type user last name in the form"""
        self.type_text(self.__last_name,lname)
    
    def type_email(self,email):
        """Type email in the form"""
        self.type_text(self.__email, email)
        
    def select_gender(self,gender):
        """select gender radio button"""
        self.click_radio_button(self.__gender_radio_list,gender)
        
    def get_gender_label_list(self):
        """get the gender label list to click element"""
        return self.get_element_list2(self.__gender_label_list)
    
    def type_mobile(self,mnumber):
        """Type the phone mobile number"""
        self.type_text(self.__mobile,mnumber)
        
    def type_date_of_birth(self,dob):
        """Enter DOB  in the format dd/mm/yyyy"""
        self.type_text(self.__dob,dob)
    
    def type_subjects(self,subject):
        """type subjec in form"""
        self.type_text(self.__subjects,subject)
    
    def select_hobbies(self, cbox):
        """select hobbies"""
        self.click_checkbox_item(self.__hobbies,cbox)
        
    def upload_file(self,path):
        """method to upload a file to the webpage"""
        self.type_text(self.__picture_file,path)
        
    def type_current_address(self, address):
        """method to entere the current address of the user"""
        self.type_text(self.__current_address,address)
        
    def select_state(self,state):
        """select state""" 
        self.type_text(self.__state,state)
    def select_city(self,city):
        """select the city """
        self.type_text(self.__city,city)
    
    def click_submit_form(self):
        """method to click submit button form"""
        self.click_element(self.__submit_button)
        
    def get_submitted_form_title(self):
        """return the element for the title after submitting the form"""
        return self.get_element(self.__title_submitted)