from helpers.api.api_client import BaseApi
from test_data.users import base_user
import pytest


@pytest.mark.parametrize('user_object', [base_user])
def test_get_api_key_for_valid_user(user_object):
    """ Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key"""
    api = BaseApi()
    status, result, _ = api.get_api_key(user_object['email'], user_object['password'])

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


@pytest.mark.parametrize('user_session_fixture', [base_user], indirect=True)
def test_get_all_pets_with_valid_key(login_custom_fixture):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    api = login_custom_fixture
    status, result = api.get_list_of_pets()

    assert status == 200
    assert len(result['pets']) > 0
