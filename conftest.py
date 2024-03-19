import pytest
import logging
import logging.config
import os
from helpers.const import PROJECT_DIR
from helpers.api.api_client import AppApi


@pytest.fixture(scope='session', autouse=True)
def setup_logging():
    """ Настраиваем логирование"""
    log_config_path = os.path.join(PROJECT_DIR, 'log_config.conf')
    logging.config.fileConfig(fname=log_config_path,
                              disable_existing_loggers=False)


@pytest.fixture(scope='class', autouse=True)  # после перехода на один логин в сьют поменяно на True
def user_session_fixture(request) -> dict:
    """ Данные текущего пользователя """
    if hasattr(request, 'param'):
        user = request.param
        logging.info(f'Получен пользователь для авторизации: email = {user["email"]} ')
        return user
    logging.warning('Не задан пользователь для авторизации')


@pytest.fixture(scope='class')
def login_custom_fixture(user_session_fixture):
    user = user_session_fixture
    email = user['email']
    password = user['password']
    logging.info(f'Логин юзером {email}')
    client = AppApi(
        email=email,
        password=password,
    )
    return client

