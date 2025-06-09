from appium import webdriver


def driver_setup():
    driver = webdriver.Remote()
    driver.get("http://localhost:4723/wd/hub")
