import pytest
from helpers.const import UPLOAD_FILES
from test_data.request_data import base_pet_data
import os


@pytest.fixture(scope='class')
def create_pet_fixture(request, login_custom_fixture):
    api = login_custom_fixture
    pet_photo = os.path.join(UPLOAD_FILES, 'dog.jpg')
    status, result = api.add_new_pet(base_pet_data['name'], base_pet_data['type'], base_pet_data['age'], pet_photo)

    def teardown():
        api.delete_pet(result['id'])

    request.addfinalizer(teardown)
    return status, result, api
