import json
import logging

import requests

from test_data.urls import base_url


class BaseApi:
    def __init__(self):
        self.base_url = base_url

    def get_api_key(self, email: str, passwd: str) -> json:
        headers = {
            'email': email,
            'password': passwd,
        }
        url = self.base_url + '/api/key'
        res = requests.get(url, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
