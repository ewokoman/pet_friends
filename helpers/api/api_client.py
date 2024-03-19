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
            self.api_key = result['key']
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result, self.api_key


class AppApi(BaseApi):
    def __init__(self, email, password):
        super().__init__()
        self.get_api_key(email, password)

    def get_list_of_pets(self, filter=""):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списком наденных питомцев, совпадающих с фильтром. На данный момент фильтр может иметь
        либо пустое значение - получить список всех питомцев, либо 'my_pets' - получить список
        собственных питомцев"""

        headers = {'auth_key': self.api_key}  # нужно значение ключа
        params = {'filter': filter}

        res = requests.get(self.base_url + '/api/pets', headers=headers, params=params)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
