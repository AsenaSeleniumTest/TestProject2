#!/usr/bin/env python3
import os
import json
import pytest
from Pages.Forms_Page import Forms_Page
from Pages.MainPage import MainPage
from Pages.Elements_Page import ElementsPage
from Utility.file_manager import File_Manager

@pytest.fixture(autouse=True,scope="function")
def read_json_file():
    """ read data from json file"""
    os.chdir("..\\TestProject2\\Tests\\Data")
    try:
        with open("formdata.json","r",encoding="utf-8") as f:
            data_1 = json.load(f)
            data_list = data_1["students"]
            return data_list
    except FileNotFoundError as file:
        return file
        
@pytest.mark.usefixtures("driver_Setup",)
class Test_form_page():

    @pytest.mark.testForm
    @pytest.mark.parametrize("test_data",read_json_file)
    def test_fill_form_male(self,driver_Setup,test_data):
        """Test method to submit a form"""
        driver = driver_Setup
        m_page=MainPage(driver)
        m_page.click_forms_page()
        e_page = ElementsPage(driver)
        f_page = e_page.click_practice_form_menu()
        title =f_page.fill_form(test_data["Name"],
                                test_data["LastName"],
                                test_data["email"],
                                test_data["gender"],
                                test_data["Mobile"],
                                test_data["BirthDate"],
                                test_data["subject"],
                                test_data["hobbies"],
                                test_data["picture"],
                                test_data["Address"],
                                test_data["state"],
                                test_data["city"])
        assert  title.text == "Thanks for submitting the form"
        
        

    