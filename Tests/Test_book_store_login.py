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
    def test_login_succesfull(self,driver_Setup):
        """Test login with valid credentials"""
        driver = driver_Setup
        main_p = MainPage(driver)
        book_store_page = main_p.click_bookstore_page()
        user = book_store_page.login_function("usuario1","Se5JiFCy@EAVAwp")
        assert user.text == "usuario1"
            
    @pytest.mark.booklist
    def test_book_list(self,driver_Setup):
        b_list =["Git Pocket Guide","Learning JavaScript Design Patterns","Designing Evolvable Web APIs with ASP.NET","Speaking JavaScript","You Don't Know JS","Programming JavaScript Applications","Eloquent JavaScript, Second Edition","Understanding ECMAScript 6"]
        driver = driver_Setup        
        mainp = MainPage(driver)
        book_store_page = mainp.click_bookstore_page()
        books = book_store_page.get_book_list()
        for i,b_item in enumerate(books):
            assert b_item.text == b_list[i]
    
    @pytest.mark.searchbook       
    def test_search_book(self,driver_Setup):
        """Test search book"""
        driver = driver_Setup
        mainp = MainPage(driver)
        book_store_page = mainp.click_bookstore_page()
        books = book_store_page.search_book("Git")
        assert books[0].text == "Git Pocket Guide"