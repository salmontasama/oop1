import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        # self.driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.get('https://ivolunteer-app.herokuapp.com/login')
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            # self.driver.close()
            self.driver.quit()

