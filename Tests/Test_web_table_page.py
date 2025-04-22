#!/usr/bin/env python3
import pytest
from Pages.MainPage import MainPage
from Pages.Elements_Page import ElementsPage
from Pages.WebTablePage import Web_Table_Page
from Configuration.TestData import TestData

@pytest.mark.usefixtures("driver_Setup")
class Test_WebTablePage():
    """Test Web Table page elements"""
    
        
    @pytest.mark.WebTableTitle
    def test_webtable_headers(self,driver_Setup):
        """ Test webtable data headers"""
        self.driver = driver_Setup
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        mainp.click_elements_page()
        elements_page = ElementsPage(self.driver)
        elements_page.click_web_tables_menu()
        wt_page = Web_Table_Page(self.driver)
        header_list = wt_page.get_header_elements()
        for elem in wt_page.get_header_elements():
            print(elem.text)
        assert len(header_list) == 7
    
    @pytest.mark.WebTableData
    def test_webtable_data(self,driver_Setup):
        """Validate data count in web table"""
        self.driver = driver_Setup
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        mainp.click_elements_page()
        elements_page = ElementsPage(self.driver)
        elements_page.click_web_tables_menu()
        wt_page = Web_Table_Page(self.driver)
        data_list = wt_page.get_data_elements()
        clean_data_list = []
        for data in data_list:
            if data.text != " ":
                clean_data_list.append(data.text)
                print(data.text)        
        assert len(clean_data_list) == 21
    
    @pytest.mark.AddRecordToWebTable
    def test_add_record_to_webtable(self,driver_Setup):
        """Add record to web table"""
        self.driver = driver_Setup
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        mainp.click_elements_page()
        elements_page = ElementsPage(self.driver)
        elements_page.click_web_tables_menu()
        wt_page = Web_Table_Page(self.driver)
        wt_page.click_add_button()
        wt_page.add_first_name("John")
        wt_page.add_last_name("Doe")
        wt_page.add_email("test2@test.com")
        wt_page.add_age("25")
        wt_page.add_salary("50000")
        wt_page.add_department("IT")
        wt_page.click_submit_form()
        data_list = wt_page.get_data_elements()
        clean_data_list = []
        found_person = ""
        for data in data_list:
            if data.text != " ":
                clean_data_list.append(data.text)
            elif data.text == "Jhon":
                found_person = data.text    
        assert "Jhon" == found_person
        
        
          