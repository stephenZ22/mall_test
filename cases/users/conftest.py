from data import users_data
import requests
from config import settings
import pytest

base_url = settings.Settings().baseUrl()
login_api_path = 'users/login'
login_url = f'{base_url}/{login_api_path}'
login_users = users_data.login_users()


@pytest.fixture
def get_user_token():
    user = login_users[0]
    header = {
        'Content-Type': 'application/json',
    }
    login_json = {
        'email': user['email'],
        'password': str(user['password']),
    }

    res = requests.post(
        login_url, headers=header, json=login_json)

    token = res.json()['token']
    return token
