#!/usr/bin/env python3
import pytest
from Pages.Forms_Page import Forms_Page
from Pages.MainPage import MainPage
from Pages.Elements_Page import ElementsPage
from Utility.file_manager import File_Manager


@pytest.mark.usefixtures("driver_Setup")
class Test_form_page():

    
    
    @pytest.mark.testForm
    @pytest.mark.parametrize("test_data","read_json_file")
    def test_fill_form_male(self,driver_Setup,test_data):
        """Test method to submit a form"""
        driver = driver_Setup
        m_page=MainPage(driver)
        f_page = Forms_Page(driver)
        e_page = ElementsPage(driver)
        m_page.click_forms_page()
        e_page.click_practice_form_menu()
        f_page.type_user_name(test_data["Name"])
        f_page.type_last_name(test_data["LastName"])
        f_page.type_email(test_data["email"])
        f_page.select_gender(test_data["gender"])
        f_page.type_mobile(test_data["Mobile"])
        f_page.type_date_of_birth(test_data["BirthDate"])
        f_page.type_subjects(test_data["subject"])
        f_page.select_hobbies(test_data["hobbies"])
        f_page.upload_file(test_data["picture"])
        f_page.type_current_address(test_data["Address"])
        f_page.select_city(test_data["state"])
        f_page.select_city(test_data["city"])
        f_page.click_submit_form()
        title = f_page.get_submitted_form_title()
        assert  title.text == "Thanks for submitting the form"
        
        

    