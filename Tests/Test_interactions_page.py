#!/usr/bin/env python3
import pytest
import selenium
from Pages.MainPage import MainPage
from Configuration.TestData import TestData
from Pages.InteractionsPage import InteractionsPage

@pytest.mark.usefixtures("driver_Setup")
class Test_interactions_page():
    """Class to test interactions page"""
    
    @pytest.mark.interactions
    def test_interactions(self, driver_Setup):
        """Test to validate the interactions page"""
        driver = driver_Setup
        driver.get(TestData.url)
        mainp = MainPage(driver)
        i_page = InteractionsPage(driver)
        mainp.click_interactions_page()
        i_page.click_sortable_menu()
        sortable_text = i_page.get_sortable_header().text
        assert sortable_text == "Sortable"
        assert "Sortable" in driver.page_source
        
    @pytest.mark.dragElement
    def test_drag_element(self, driver_Setup):
        """Test to validate the drag element"""
        driver = driver_Setup
        driver.get("https://demoqa.com/")
        mainp = MainPage(driver)
        i_page = InteractionsPage(driver)
        mainp.click_interactions_page()
        i_page.click_sortable_menu()
        i_page.drag_one_to_three()
        assert "Sortable" in driver.page_source
    
    @pytest.mark.draggable_list
    def test_get_sortable_list(self,driver_Setup):
        """Test to validate the sortable list"""
        driver = driver_Setup
        driver.get(TestData.url)
        mainp = MainPage(driver)
        i_page = InteractionsPage(driver)
        mainp.click_interactions_page()
        i_page.click_sortable_menu()    
        sortable_list = i_page.get_sortable_list()
        assert len(sortable_list) == 6