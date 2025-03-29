from pages.Dummyticketpage import Dummyticketpage
import pytest
import time

@pytest.mark.usefixtures("setup_and_teardown")
class TestDummyticket:


    def test_dummyticket(self):
        dummypage = Dummyticketpage(self.driver)
        dummypage.launch_dummyticketpage()
        dummypage.enter_first_name()
        dummypage.enter_last_name()
        # dummypage.select_DOB()
        # dummypage.select_day_dob()
        dummypage.click_male_radio_btn()
        dummypage.enter_from_city()
        dummypage.enter_to_city()
        time.sleep(5)
