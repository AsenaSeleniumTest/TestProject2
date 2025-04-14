import pytest
from Pages.MainPage import MainPage
from Pages.Elements_Page import ElementsPage
from Pages.CheckBoxPage import CheckBoxPage
from Configuration.TestData import TestData
from log_config import logger

@pytest.mark.usefixtures("driver_Setup")
class Test_CheckBoxPage():
    """Test Check Box page elements"""
    driver = None

    @pytest.mark.CheckBoxTitle
    def test_checkboxtitle(self,driver_Setup):    
        """Checks the Check Box title is displayed"""
        self.driver = driver_Setup 
        self.driver.get(TestData.url) 
        mainp =MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        checkBoxPage= CheckBoxPage(self.driver)
        mainp.click_elements_page()
        elements_page.click_check_box()
        checkBoxPage.click_expand_all()
        texto = checkBoxPage.get_check_box_title().text
        logger.info(f"Check Box title is {texto}")
        assert texto == "Check Box"
        

    @pytest.mark.ChecBoxDesktop
    def test_desktop_menu_present(self,driver_Setup):
        """Checks the Desktop menu option is dispplayed"""
        self.driver = driver_Setup
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        checkBoxPage= CheckBoxPage(self.driver)
        mainp.click_elements_page()
        elements_page.click_check_box()
        checkBoxPage.click_expand_all()
        assert checkBoxPage.desktop_is_displayed() == True
         
    @pytest.mark.CheckBoxDocuments
    def test_documents_menu_present(self,driver_Setup):
        """Checks the Documents menu option is displayed"""
        self.driver = driver_Setup
        self.driver.get(TestData.url)
        mainp = MainPage(self.driver)
        elements_page = ElementsPage(self.driver)
        check_Box_Page= CheckBoxPage(self.driver)
        mainp.click_elements_page()
        elements_page.click_check_box()
        check_Box_Page.click_expand_all()
        assert check_Box_Page.documents_is_displayed() is True    