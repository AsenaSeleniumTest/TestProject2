#!/usr/bin/env python3
import sys

class TestData:
    SCROLL_FULL_HEIGTH = "window.scrollTo(0, document.body.scrollHeight);"
    SCROLL_PARTIAL_HEIGHT = "window.scrollTo(0, document.body.scrollHeight/2);"
    SCROLL_FULL_WIDTH = "window.scrollTo(document.body.scrollWidth, 0);"
    url = "https://demoqa.com/"
    username = "testuser"
    password = "testpassword"
    invalid_username = "invaliduser"
    full_name = "USB Test Sr Manual"
    email = "testemail@test.com"
    current_address = "123 Test Street, Test City, Test State, 12345"
    Permanent_address = "456 Test Avenue, Test City, Test State, 67890"
    
    
if __name__ == "__main__":
    print("TestData module is not meant to be run directly.")
    print("It is intended to be imported and used in other test modules.")
   