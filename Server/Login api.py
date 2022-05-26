import pytest
import requests


class Test_loginapi():
    def test_valid_login(self):
        url = "https://ivolunteer-app.herokuapp.com/users/login"
        myobj = {"Email": "salmon997@walla.co.il", "Password": "123456"}
        x = requests.post(url, data=myobj)
        print(x)
        assert x.status_code == 500
        assert x.elapsed.total_seconds() < 7

    def test_requests_invalid_login_null_email(self):
        url = "https://ivolunteer-app.herokuapp.com/users/login"
        myobj = {"Email": "", "Password": "123456"}
        x = requests.post(url, data=myobj)
        print(x)
        assert x.status_code == 500
        assert x.elapsed.total_seconds() < 7


    def test_requests_invalid_login_null_password(self):
        url = "https://ivolunteer-app.herokuapp.com/users/login"
        myobj = {"Email": "salmon997@walla.co.il", "Password": ""}
        x = requests.post(url, data=myobj)
        print(x)
        assert x.status_code == 500
        assert x.elapsed.total_seconds() < 7
