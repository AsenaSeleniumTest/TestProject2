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
driver = None

@pytest.fixture(autouse=True, params=["chrome"], scope="class")
def driver_Setup(request):
    """ Setup the driver for the test """
    
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

def _capture_screenshot(file_name):
    """Capture screenshot and save it to the specified file"""
    driver.get_screenshot_as_file(file_name)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """Hook to take screenshot on test failure"""
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    
    if report.when =="call" and report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if(report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), "Reports")
            file_name = os.path.join(reports_dir, report.nodeid.replace("::","_") + ".png")
            print("file name is : " + file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = f'<div><img src="{file_name}" alt="screenshot" style="width: 300px;"/></div>'
                extra.append(pytest_html.extras.html(html))
    report.extra = extra
                