
from config import settings
import requests
import pytest
from data import users_data

url = settings.Settings().testUrl()
base_url = settings.Settings().baseUrl()
login_api_path = 'users/login'
login_url = f'{base_url}/{login_api_path}'


def get_users_login_items():
    items = []
    login_users = users_data.login_users()
    for user in login_users:
        items.append([user['email'], user['password']])

    return items


@pytest.mark.parametrize("email,password", get_users_login_items())
def test_user_login(email, password):
    header = {
        'Content-Type': 'application/json',
    }
    login_json = {
        'email': email,
        'password': str(password),
    }

    res = requests.post(
        login_url, headers=header, json=login_json)

    result = res.json()
    assert result['token'] is not None
    assert result['message'] == 'ok'
    assert res.status_code == 200


def test_create_user_ok():
    r = requests.get(url)

    assert r.status_code == 200


def test_create_user_failed():
    pass


# "http://xxxxx/users"
def test_get_all_users(get_user_token):
    token = get_user_token
    user_info_url = f'{base_url}/users'
    res = requests.get(user_info_url, headers={'Authorization': token})
    result = res.json()

    assert res.status_code == 200
    assert result['message'] == 'ok'
    assert result['data'] is not None


def test_get_user_info_failed():
    pass


if __name__ == "__main__":
    pytest.main([__file__])
