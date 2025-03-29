from re import findall

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.Basepage import Basepage


class Dummyticketpage(Basepage):

    def __init__(self,driver):
        super().__init__(driver)

    coupon_radio_button_xpath = "//*[@id='product_551']"
    first_name_xpath = "//*[@id='travname']"
    last_name_xpath = "//*[@id='travlastname']"
    date_of_birth_xpath = "//*[@id='dob']"
    year_dob_xpath = "//*[@id='ui-datepicker-div']/div[1]/div/select[2]"
    month_dob_xpath = "//*[@id='ui-datepicker-div']/div[1]/div/select[1]"
    date_xpath = "//*[@id='ui-datepicker-div']/table/tbody/tr/td"
    male_radio_button_xpath = "//*[@id='sex_1']"
    from_city_textbox_xpath = "//*[@id='fromcity']"
    to_city_textbox_xpath = "//*[@id='tocity']"


    def launch_dummyticketpage(self):
        self.driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

    def click_coupon_radio_button(self):
        self.click_to_element("coupon_radio_button_xpath",self.coupon_radio_button_xpath)


    def enter_first_name(self):
        self.type_to_element("Rahul...","first_name_xpath",self.first_name_xpath)
    def enter_last_name(self):
        self.type_to_element("gupta...", "last_name_xpath", self.last_name_xpath)

    def select_DOB(self):
        self.click_to_element("date_of_birth_xpath",self.date_of_birth_xpath)
        years = self.get_element("year_dob_xpath",self.year_dob_xpath)
        months = self.get_element("month_dob_xpath",self.month_dob_xpath)
        allyears = Select(years)
        allyears.select_by_visible_text("1996")
        allmonth = Select(months)
        allmonth.select_by_visible_text("Jan")

    def select_day_dob(self):
        rows_xpath = "//table[@class = 'ui-datepicker-calendar']/tbody/tr"
        column_xpath ="//table[@class = 'ui-datepicker-calendar']/tbody/tr[1]/td"
        rows = self.driver.find_element(By.XPATH,rows_xpath)
        column = self.driver.find_element(By.XPATH,column_xpath)
        day_xpath = "//*[@id='ui-datepicker-div']/table/tbody/tr[4]/td[7]/a"
        self.click_to_element("day_xpath",day_xpath)

    def click_male_radio_btn(self):
        self.click_to_element("male_radio_button_xpath",self.male_radio_button_xpath)

    def enter_from_city(self):
        self.type_to_element("Delhi","from_city_textbox_xpath",self.from_city_textbox_xpath)
    def enter_to_city(self):
        self.type_to_element("Mumbai","to_city_textbox_xpath",self.to_city_textbox_xpath)


