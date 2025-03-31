import pytest
from Pages.BasePage import BasePage
from Pages.MainPage import MainPage
from log_config import logger

@pytest.mark.usefixtures("driver_Setup")
class Test_Main_Page():
    """Test Main page elements"""
    driver = None

    @pytest.mark.WelcomeTitle
    def test_welcometitle(self,driver_Setup):    
        self.driver = driver_Setup 
        bPage=BasePage(self.driver)
        mainp =MainPage(self.driver)
        logger.info("Browser opened ")
        assert mainp.title_displayed == True
