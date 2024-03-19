import json
import logging

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

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
        logging.info(self.api_key)
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

    def add_new_pet(self, name, animal_type,
                    age, pet_photo_path):
        """Метод отправляет  на сервер данные о добавляемом питомце и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца"""
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo_path, open(pet_photo_path, 'rb'), 'image/jpg')
            })
        headers = {'auth_key': self.api_key, 'Content-Type': data.content_type}

        res = requests.post(self.base_url + '/api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        logging.info(result)
        return status, result

    def delete_pet(self, pet_id):
        """Метод удаляет питомца по id """
        headers = {'auth_key': self.api_key}
        res = requests.delete(self.base_url + f'/api/pets/{pet_id}', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        logging.info(result)
        return status, result
