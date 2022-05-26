import time

import allure
from Web.Pages.LoginPage import LoginPage
import pytest
# import pandas as pd
from Web.Locator.MainProvideAssistanceLocators import MainProvideLocators as MA
from Web.Base.base import Base


@pytest.mark.usefixtures('set_up')
class Test_Login(Base):

    # __user_data_file = r"\login_details.xlsx"
    # df = pd.read_excel(os.getcwd() + __user_data_file)
    @pytest.mark.sanity
    def test_valid_login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email(MA.valid_email)
        login.enter_password(MA.valid_password)
        login.click_send()


    @allure.step
    def test_invalid_login_null_email(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_password(MA.valid_password)
        login.click_send()
        time.sleep(5)
        x = driver.switch_to.alert
        a = x.text
        assert a == "Check your password or email"


    def test_invalid_login_null_password(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email(MA.valid_email)
        login.click_send()
        time.sleep(5)
        x = driver.switch_to.alert
        a = x.text
        assert a == "Check your password or email"
# djcfnsdjcbsdjafhjsd,avhjdsav
# fbvefwsbgrtte
# ewfbefwbgveaw
# dfhbehbsdghb
#fdfvdkh;l515