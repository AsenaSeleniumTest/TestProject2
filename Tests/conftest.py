#!/usr/bin/env python3
import json
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Configuration.TestData import TestData
from Utility.file_manager import File_Manager


@pytest.fixture(autouse=True, params=["chrome"], scope="class")
def driver_Setup(request):
    """ Setup the driver for the test """
    driver = None
    if request.param == "chrome":
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
       # options.add_argument("headless")
        options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(service = service,options = options)
        driver.maximize_window()
        driver.get(TestData.url)
    elif request.param == "edge":
        service = Service(EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service = service,options = options)
        driver.get(TestData.url)
    else:
        raise WebDriverException("Unsupported browser:" + format(request.param))
    yield driver
    driver.close()

@pytest.fixture(autouse=True,scope="class")
def data_forms():
    data_file = File_Manager("C:\\users\\formusers.xlsx")
    datalist = data_file.read_excel_file()
    return datalist
