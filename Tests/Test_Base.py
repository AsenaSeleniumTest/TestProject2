#!/usr/bin/env python3
import pytest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Pages.MainPage import MainPage
from Pages.CheckBoxPage import CheckBoxPage


@pytest.mark.usefixtures("driver_Setup")
class Test_Base:
    """_summary_

    Returns:
        _type_: _description_
        pytest --html='report3.html' -v -s -n 2   to run the tests in parallel with 2 workers
        and  html report generated
    """
    driver = None
    
    @pytest.fixture(scope='package',autouse=True)
    def setup_checkbox(self,driver_Setup):
        """_summary_: set up driver to run tests
        """
        self.driver = driver_Setup
        check_box_page = CheckBoxPage(self.driver)
        return check_box_page
        
    @pytest.fixture(scope='class',autouse=True,params=["chrome"])
    def setup(self,request):
        """_summary_: set up driver to run tests
        """
        if request.param == "chrome":
            service = Service(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service = service, options=options)
            self.driver.maximize_window()
           
        elif request.param == "edge":
            
            service = Service(EdgeChromiumDriverManager().install())
            options = webdriver.EdgeOptions()
            self.driver = webdriver.Edge(service = service, options = options)
            self.driver.maximize_window()
            
        return self.driver

    