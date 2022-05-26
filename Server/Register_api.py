import pytest
import requests


class Test_register_valid():
    def test_valid_register(self):
        url = "https://ivolunteer-app.herokuapp.com/users/register"
        myobj = {"Email":"salmon7@walla.co.il","Password":"123456","FirstName":"asds","LastName":"sdaaasdas","Age":"32","ProfilePic":"adfad"}
        x = requests.post(url, json=myobj)
        print(x.text)
        assert x.status_code == 200
        assert x.elapsed.total_seconds() < 7