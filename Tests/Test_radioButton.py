#!/usr/bin/env python3
import pytest
from Pages.MainPage import MainPage
from Pages.Elements_Page import ElementsPage
from Pages.RadioButtonPage import Radio_Button_Page
from Configuration.TestData import TestData


@pytest.mark.usefixtures("driver_Setup")
class Test_Radio_Button_Page():
    """Test Radio Button page elements"""
    driver = None

    @pytest.mark.RadioButtonTitle
    def test_radiobutton_title(self, driver_Setup):
        """Checks the Radio Button title is displayed"""
        self.driver = driver_Setup
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        radio_button_page = Radio_Button_Page(self.driver)
        mainp.click_elements_page()
        elements_page.click_radio_button_menu()
        texto = radio_button_page.get_radio_button_title()
        
        assert texto.text == "Radio Button"
        
    @pytest.mark.RadioButtonYes
    def test_radio_button_yes(self, driver_Setup):
        """Checks the Radio Button Yes is displayed"""
        self.driver = driver_Setup
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        radio_p= Radio_Button_Page(self.driver)
        mainp.click_elements_page()
        elements_page.click_radio_button_menu()
        radio_p.click_radio_button_yes()
        value = radio_p.get_you_have_selected_label()
        opt_value = radio_p.get_span_selected_yes()
        assert value.text == "You have selected Yes"
        assert opt_value.text == "Yes"
    
    @pytest.mark.RadioButtonImpressive
    def test_radio_button_impressive(self, driver_Setup):
        """Checks the Radio Button Impressive is displayed"""
        self.driver = driver_Setup
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        radio_p= Radio_Button_Page(self.driver)
        mainp.click_elements_page()
        elements_page.click_radio_button_menu()
        radio_p.click_radio_button_impressive()
        value = radio_p.get_you_have_selected_label()
        opt_value = radio_p.get_span_selected_impressive()
        assert value.text == "You have selected Impressive"
        assert opt_value.text == "Impressive"    