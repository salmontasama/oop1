# import sys, os
# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, myPath + '/../')
from time import sleep

from Web.Pages.ProvideAssistance import ProvidePage
from Web.Base.base import Base
import pytest
# import pandas as pd
from Web.Locator.MainProvideAssistanceLocators import MainProvideLocators as MA
import allure


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures('set_up')
class Test_Sending_Volunteer(Base):

    # __user_data_file = r"\login_details.xlsx"
    # df = pd.read_excel(os.getcwd() + __user_data_file)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_Sending_volunteering(self):
        driver = self.driver
        provide = ProvidePage(driver)
        provide.enter_email(MA.valid_email)
        provide.enter_password(MA.valid_password)
        provide.click_send()
        sleep(10)
        driver.switch_to.alert.accept()
        provide.click_provide_assistance()
        provide.enter_name('salmon')
        provide.enter_last_name('tasama')
        provide.enter_age('24')
        provide.enter_skills('Adult help')
        provide.enter_start_hour('9:00')
        provide.enter_finish_hour('19:00')
        provide.enter_phone_number('054787777')
        provide.enter_profile_pic(
            'https://upload.wikimedia.org/wikipedia/commons/4/42/Solar_prominence_from_STEREO_spacecraft_September_29%2C_2008.jpg')
        provide.enter_language('Hebrew')
        provide.enter_description('Nursing Home')
        provide.click_send_button_pv()

        try:
            assert "iVolunteer" == driver.title
        except Exception as e:
            raise
            print("Title is wrong", format(e))

    def test_invalid_Sending_volunteering_null_name(self):
        driver = self.driver
        provide = ProvidePage(driver)
        provide.enter_email(MA.valid_email)
        provide.enter_password(MA.valid_password)
        provide.click_send()
        sleep(10)
        driver.switch_to.alert.accept()
        provide.click_provide_assistance()
        provide.enter_last_name('tasama')
        provide.enter_age('24')
        provide.enter_skills('Adult help')
        provide.enter_start_hour('9:00')
        provide.enter_finish_hour('19:00')
        provide.enter_phone_number('054787777')
        provide.enter_profile_pic(
            'https://upload.wikimedia.org/wikipedia/commons/4/42/Solar_prominence_from_STEREO_spacecraft_September_29%2C_2008.jpg')
        provide.enter_language('Hebrew')
        provide.enter_description('Nursing Home')
        provide.click_send_button_pv()

    def test_invalid_Sending_volunteering_null_lastname(self):
        driver = self.driver
        provide = ProvidePage(driver)
        provide.enter_email(MA.valid_email)
        provide.enter_password(MA.valid_password)
        provide.click_send()
        sleep(5)
        driver.switch_to.alert.accept()
        provide.click_provide_assistance()
        provide.enter_name('salmon')
        provide.enter_age('24')
        provide.enter_skills('Adult help')
        provide.enter_start_hour('9:00')
        provide.enter_finish_hour('19:00')
        provide.enter_phone_number('054787777')
        provide.enter_profile_pic(
            'https://upload.wikimedia.org/wikipedia/commons/4/42/Solar_prominence_from_STEREO_spacecraft_September_29%2C_2008.jpg')
        provide.enter_language('Hebrew')
        provide.enter_description('Nursing Home')
        provide.click_send_button_pv()

    def test_invalid_Sending_volunteering_null_age(self):
        driver = self.driver
        provide = ProvidePage(driver)
        provide.enter_email(MA.valid_email)
        provide.enter_password(MA.valid_password)
        provide.click_send()
        sleep(3)
        driver.switch_to.alert.accept()
        provide.click_provide_assistance()
        provide.enter_name('salmon')
        provide.enter_last_name('tasama')
        provide.enter_skills('Adult help')
        provide.enter_start_hour('9:00')
        provide.enter_finish_hour('19:00')
        provide.enter_phone_number('054787777')
        provide.enter_profile_pic(
            'https://upload.wikimedia.org/wikipedia/commons/4/42/Solar_prominence_from_STEREO_spacecraft_September_29%2C_2008.jpg')
        provide.enter_language('Hebrew')
        provide.enter_description('Nursing Home')
        provide.click_send_button_pv()

    def test_invalid_Sending_volunteering_null_skills(self):
        driver = self.driver
        provide = ProvidePage(driver)
        provide.enter_email(MA.valid_email)
        provide.enter_password(MA.valid_password)
        provide.click_send()
        sleep(3)
        driver.switch_to.alert.accept()
        provide.click_provide_assistance()
        provide.enter_name('salmon')
        provide.enter_last_name('tasama')
        provide.enter_age('24')
        provide.enter_start_hour('9:00')
        provide.enter_finish_hour('19:00')
        provide.enter_phone_number('054787777')
        provide.enter_profile_pic(
            'https://upload.wikimedia.org/wikipedia/commons/4/42/Solar_prominence_from_STEREO_spacecraft_September_29%2C_2008.jpg')
        provide.enter_language('Hebrew')
        provide.enter_description('Nursing Home')
        provide.click_send_button_pv()

    def test_invalid_Sending_volunteering_null_start_hour(self):
        driver = self.driver
        provide = ProvidePage(driver)
        provide.enter_email(MA.valid_email)
        provide.enter_password(MA.valid_password)
        provide.click_send()
        sleep(3)
        driver.switch_to.alert.accept()
        provide.click_provide_assistance()
        provide.enter_name('salmon')
        provide.enter_last_name('tasama')
        provide.enter_age('24')
        provide.enter_skills('Adult help')
        provide.enter_finish_hour('19:00')
        provide.enter_phone_number('054787777')
        provide.enter_profile_pic(
            'https://upload.wikimedia.org/wikipedia/commons/4/42/Solar_prominence_from_STEREO_spacecraft_September_29%2C_2008.jpg')
        provide.enter_language('Hebrew')
        provide.enter_description('Nursing Home')
        provide.click_send_button_pv()

    def test_invalid_Sending_volunteering_null_finish_hour(self):
        driver = self.driver
        provide = ProvidePage(driver)
        provide.enter_email(MA.valid_email)
        provide.enter_password(MA.valid_password)
        provide.click_send()
        sleep(5)
        driver.switch_to.alert.accept()
        provide.click_provide_assistance()
        provide.enter_name('salmon')
        provide.enter_last_name('tasama')
        provide.enter_age('24')
        provide.enter_skills('Adult help')
        provide.enter_start_hour('9:00')
        provide.enter_phone_number('054787777')
        provide.enter_profile_pic(
            'https://upload.wikimedia.org/wikipedia/commons/4/42/Solar_prominence_from_STEREO_spacecraft_September_29%2C_2008.jpg')
        provide.enter_language('Hebrew')
        provide.enter_description('Nursing Home')
        provide.click_send_button_pv()

    def test_invalid_Sending_volunteering_null_phon_number(self):
        driver = self.driver
        provide = ProvidePage(driver)
        provide.enter_email(MA.valid_email)
        provide.enter_password(MA.valid_password)
        provide.click_send()
        sleep(5)
        driver.switch_to.alert.accept()
        provide.click_provide_assistance()
        provide.enter_name('salmon')
        provide.enter_last_name('tasama')
        provide.enter_age('24')
        provide.enter_skills('Adult help')
        provide.enter_start_hour('9:00')
        provide.enter_finish_hour('19:00')
        provide.enter_profile_pic(
            'https://upload.wikimedia.org/wikipedia/commons/4/42/Solar_prominence_from_STEREO_spacecraft_September_29%2C_2008.jpg')
        provide.enter_language('Hebrew')
        provide.enter_description('Nursing Home')
        provide.click_send_button_pv()

    def test_invalid_Sending_volunteering_null_profile_pic(self):
        driver = self.driver
        provide = ProvidePage(driver)
        provide.enter_email(MA.valid_email)
        provide.enter_password(MA.valid_password)
        provide.click_send()
        sleep(5)
        driver.switch_to.alert.accept()
        provide.click_provide_assistance()
        provide.enter_name('salmon')
        provide.enter_last_name('tasama')
        provide.enter_age('24')
        provide.enter_skills('Adult help')
        provide.enter_start_hour('9:00')
        provide.enter_finish_hour('19:00')
        provide.enter_phone_number('054787777')
        provide.enter_language('Hebrew')
        provide.enter_description('Nursing Home')
        provide.click_send_button_pv()

    def test_invalid_Sending_volunteering_null_language(self):
        driver = self.driver
        provide = ProvidePage(driver)
        provide.enter_email(MA.valid_email)
        provide.enter_password(MA.valid_password)
        provide.click_send()
        sleep(5)
        driver.switch_to.alert.accept()
        provide.click_provide_assistance()
        provide.enter_name('salmon')
        provide.enter_last_name('tasama')
        provide.enter_age('24')
        provide.enter_skills('Adult help')
        provide.enter_start_hour('9:00')
        provide.enter_finish_hour('19:00')
        provide.enter_phone_number('054787777')
        provide.enter_profile_pic(
            'https://upload.wikimedia.org/wikipedia/commons/4/42/Solar_prominence_from_STEREO_spacecraft_September_29%2C_2008.jpg')
        provide.enter_description('Nursing Home')
        provide.click_send_button_pv()

    def test_invalid_Sending_volunteering_null_discription(self):
        driver = self.driver
        provide = ProvidePage(driver)
        provide.enter_email(MA.valid_email)
        provide.enter_password(MA.valid_password)
        provide.click_send()
        sleep(3)
        driver.switch_to.alert.accept()
        provide.click_provide_assistance()
        provide.enter_name('salmon')
        provide.enter_last_name('tasama')
        provide.enter_age('24')
        provide.enter_skills('Adult help')
        provide.enter_start_hour('9:00')
        provide.enter_finish_hour('19:00')
        provide.enter_phone_number('054787777')
        provide.enter_profile_pic(
            'https://upload.wikimedia.org/wikipedia/commons/4/42/Solar_prominence_from_STEREO_spacecraft_September_29%2C_2008.jpg')
        provide.enter_language('Hebrew')
        provide.click_send_button_pv()
