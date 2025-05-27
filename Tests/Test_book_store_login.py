#!/usr/bin/env python3
import pytest
from Pages.MainPage import MainPage

@pytest.mark.usefixtures("driver_Setup")
class Test_book_store_login():
    """Class to test book store login and creaction of user"""
    @pytest.mark.bookstorelogin
    def test_invalid_login(self, driver_Setup):
        """Test invalid login"""
        driver = driver_Setup
        mainp = MainPage(driver)
        book_store_page = mainp.click_bookstore_page()
        message = book_store_page.login_function_invalid("invalid_user", "invalid_password")
        assert message.text == "Invalid username or password!"
    
    @pytest.mark.bookstorelogin
    def test_create_user(self, driver_Setup):
        """Test create user"""
        driver = driver_Setup
        mainp = MainPage(driver)
        book_store_page = mainp.click_bookstore_page()
        message = book_store_page.create_user("John", "Doe", "john_doe", "Password123!")
        assert message == "User created successfully."    