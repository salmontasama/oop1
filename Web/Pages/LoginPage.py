import allure
from selenium.webdriver.common.by import By

from Web.Locator.MainProvideAssistanceLocators import MainProvideLocators as MA


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_field = MA.email_field_login
        self.password_field = MA.password_field_login
        self.send_button = MA.send_button_login
    @allure.step
    def enter_email(self, email):
        self.driver.find_element(By.XPATH,self.email_field).send_keys(email)
    @allure.step
    def enter_password(self, password):
        self.driver.find_element(By.XPATH,self.password_field).send_keys(password)
    @allure.step
    def click_send(self):
        self.driver.find_element(By.XPATH,self.send_button).click()
