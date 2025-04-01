import pytest
from Pages.MainPage import MainPage
from Pages.Elements_Page import ElementsPage
from log_config import logger

@pytest.mark.usefixtures("driver_Setup")
class Test_ElementsPage():
    """Test Elements page elements"""
    driver = None
    mainp = None
    elements_page = None
   

    @pytest.mark.ElementsTitle
    def test_elementstitle(self,driver_Setup):    
        self.driver = driver_Setup
        mainp = MainPage(self.driver)
    
        mainp.click_elements_page()
        logger.info("Browser opened ")
        assert self.driver.title == "DEMOQA"
        assert self.driver.get_current_window() == self.driver.current_window_handle

    @pytest.mark.ElementsMenu
    def test_elementsmenu_count(self,driver_Setup):    
        """Test Elements page elements"""     
        self.driver = driver_Setup 
        mainp = MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        logger.info(f"Clicking on elements menu: {mainp.__class__}")
        mainp.click_elements_page(self)
        
        list_menu = elements_page.get_menu_list_elements()
        assert len(list_menu) == 9
        
    @pytest.mark.ElementsMenu  
    def test_click_text_box(self,driver_Setup):    
        """Test Elements page elements"""     
        self.driver = driver_Setup 
        mainp = MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        logger.info(f"Clicking on elements menu: {mainp.__class__}")
        mainp.click_elements_page(self)
        elements_page.click_text_box()
        