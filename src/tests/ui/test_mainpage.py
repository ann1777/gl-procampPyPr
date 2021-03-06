import pytest

from src.pageobjects.mainpage import MainPage

class TestLoginPage:
    @pytest.assert.story('check_title_presence')
    def test_check_title(self, driver):
        loginpage = LoginPage(driver)
        assert loginpage.is_block_title_present(), 'title is not present on the mainpage'


import requests
import json


def test_post_headers_body_json():
    url = 'https://httpbin.org/post'

    # Additional headers.
    headers = {'Content-Type': 'application/json'}

    # Body
    payload = {'key1': 1, 'key2': 'value2'}

    # convert dict to json string by json.dumps() for body data.
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['url'] == url

    # print response full body as text
    print(resp.text)