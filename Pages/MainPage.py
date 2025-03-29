import selenium.webdriver as webdriver
import selenium.webdriver.common.by as By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from Pages.BasePage import BasePage

class MainPage(BasePage):
    welcome_title = (By.XPATH,"//h1[contains(text(),'Welcome to BPB Online')]")
    myaccount_link = (By.LINK_TEXT, "My Account")
    checkout_link = (By.LINK_TEXT, "Checkout")
    cart_content = (By.XPATH, "//div[@id='headerShortcuts']//span[contains(text(),'Cart Contents')]")
    
    def __init__(self, driver):
        super().__init__(driver)

    def title_displayed(self):
        return BasePage.element_status_displayed(self.welcome_title).displayed