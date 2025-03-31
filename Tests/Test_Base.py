import pytest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Pages.BasePage import BasePage


class Test_Base:
    driver = None
    HOME_URL="https://demoqa.com/"
    @pytest.fixture(scope='class',autouse=True,params=["chrome"]) 
    def setup(self,request):
        if request.param == "chrome":
            self.service = Service(ChromeDriverManager().install())
            self.options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=self.service,options=self.options)
            self.driver.maximize_window()
           
        elif request.param == "edge":
            self.service = Service(EdgeChromiumDriverManager().install())
            self.options = webdriver.EdgeOptions()
            self.driver = webdriver.Edge(service = self.service,options = self.options)
            self.driver.maximize_window()
            
        return self.driver

    