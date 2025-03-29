from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_selected


class Basepage:

    def __init__(self,driver):
        self.driver = driver


    def get_element(self,locator_name, locator_value):
        global element
        if locator_name.endswith("xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("class"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        else:
            print("please select appropriate locator>>>>>")
        return element

    def type_to_element(self,value,locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(value)


    def click_to_element(self,locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()

    def get_element_text(self,locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.text