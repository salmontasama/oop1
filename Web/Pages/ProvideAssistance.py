import allure

from Web.Locator.MainProvideAssistanceLocators import MainProvideLocators as MA
from selenium.webdriver.common.by import By


class ProvidePage:

    def __init__(self, driver):
        self.driver = driver
        self.email_field = MA.email_field_login
        self.password_field = MA.password_field_login
        self.send_button = MA.send_button_login
        self.provide_assistance = MA.provide_assistance
        self.name_field = MA.name_field
        self.last_name_field = MA.last_name_field
        self.age_field = MA.age_field
        self.skills_field = MA.skills_field
        self.start_hour_field = MA.start_hour_field
        self.finish_hour_field = MA.finish_hour_field
        self.phone_number_field = MA.phone_number_field
        self.profile_pic_field = MA.profile_pic_field
        self.language_field = MA.language_field
        self.description_field = MA.description_field
        self.send_button_pv_page = MA.send_button_pv_page

    @allure.step('valid email')
    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_field).send_keys(email)

    @allure.step
    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_field).send_keys(password)

    @allure.step
    def click_send(self):
        self.driver.find_element(By.XPATH, self.send_button).click()

    @allure.step
    def click_provide_assistance(self):
        self.driver.find_element(By.XPATH, self.provide_assistance).click()

    @allure.step
    def enter_name(self, name):
        # self.driver.find_element_by_name(self.name_field).clear()
        self.driver.find_element(By.XPATH, self.name_field).send_keys(name)

    @allure.step
    def enter_last_name(self, last_name):
        # self.driver.find_element_by_name(self.last_name_field).clear()
        self.driver.find_element(By.XPATH, self.last_name_field).send_keys(last_name)

    @allure.step
    def enter_age(self, age):
        # self.driver.find_element_by_name(self.age_field).clear()
        self.driver.find_element(By.XPATH, self.age_field).send_keys(age)

    @allure.step
    def enter_skills(self, skills):
        # self.driver.find_element_by_name(self.skills_field).clear()
        self.driver.find_element(By.XPATH, self.skills_field).send_keys(skills)

    @allure.step
    def enter_start_hour(self, start_hour):
        # self.driver.find_element_by_name(self.start_hour_field).clear()
        self.driver.find_element(By.XPATH, self.start_hour_field).send_keys(start_hour)

    @allure.step
    def enter_finish_hour(self, finish_hour):
        # self.driver.find_element_by_name(self.finish_hour_field).clear()
        self.driver.find_element(By.XPATH, self.finish_hour_field).send_keys(finish_hour)

    @allure.step
    def enter_phone_number(self, phone_number):
        # self.driver.find_element_by_name(self.phone_number_field).clear()
        self.driver.find_element(By.XPATH, self.phone_number_field).send_keys(phone_number)

    @allure.step
    def enter_profile_pic(self, profile_pic):
        # self.driver.find_element_by_name(self.profile_pic_field).clear()
        self.driver.find_element(By.XPATH, self.profile_pic_field).send_keys(profile_pic)

    @allure.step
    def enter_language(self, language):
        # self.driver.find_element_by_name(self.language_field).clear()
        self.driver.find_element(By.XPATH, self.language_field).send_keys(language)

    @allure.step
    def enter_description(self, description):
        # self.driver.find_element_by_name(self.description_field).clear()
        self.driver.find_element(By.XPATH, self.description_field).send_keys(description)

    def click_send_button_pv(self):
        self.driver.find_element(By.XPATH, self.send_button_pv_page).click()
