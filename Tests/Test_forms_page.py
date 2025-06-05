#!/usr/bin/env python3
import os
import json
import pytest
from Pages.Forms_Page import Forms_Page
from Pages.MainPage import MainPage
from Pages.Elements_Page import ElementsPage

        
@pytest.mark.usefixtures("driver_Setup")
class Test_form_page():

    @pytest.mark.skip(reason="Skip this test")
    @pytest.mark.testForm
    
    def test_fill_form_male(self,driver_Setup):
        """Test method to submit a form"""
        driver = driver_Setup
        m_page=MainPage(driver)
        m_page.click_forms_page()
        e_page = ElementsPage(driver)
        f_page = e_page.click_practice_form_menu()
        title =f_page.fill_form(["Name"],
                                ["LastName"],
                                ["email"],
                                ["gender"],
                                ["Mobile"],
                                ["BirthDate"],
                                ["subject"],
                                ["hobbies"],
                                ["picture"],
                                ["Address"],
                                ["state"],
                                ["city"])
        assert  title.text == "Thanks for submitting the form"
        
        

    