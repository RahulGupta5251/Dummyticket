import pytest
import time
from selenium import webdriver
from utilitiles.ReadConfigurations import readconfigurations



@pytest.fixture()
def setup_and_teardown(request):
    browser = readconfigurations("basic_info","browser")
    if browser =="chrome":
        driver = webdriver.Chrome()
    elif browser =="edge":
        driver = webdriver.Edge()
    elif browser =="firefox":
        driver = webdriver.Firefox()
    else:
        print("Please select correct web browser ......")

    # dummyticketurl = readconfigurations("basic_info","url")
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(10)
    yield driver
    driver.quit()

