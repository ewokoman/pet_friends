from helpers.api.api_client import BaseApi
from test_data.users import base_user
import pytest


@pytest.mark.parametrize('user_object', [base_user])
def test_get_api_key_for_valid_user(user_object):
    """ Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key"""
    api = BaseApi()
    status, result = api.get_api_key(user_object['email'], user_object['password'])

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result