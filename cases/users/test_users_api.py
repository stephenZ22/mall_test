
from config import settings
import requests
import pytest
from data import users_data

# setting = settings.Settings()
# print(setting.baseUrl())

# @pytest.mar
url = settings.Settings().testUrl()
base_url = settings.Settings().baseUrl()
login_api_path = 'users/login'
login_url = f'{base_url}/{login_api_path}'


def get_users_login_items():
    items = []
    login_users = users_data.login_users()
    print(login_users)
    for user in login_users:
        items.append([user['email'], user['password']])

    return items


@pytest.mark.parametrize("email,password", get_users_login_items())
def test_user_login(email, password):
    header = {
        'Content-Type': 'application/json',
        # 'User-Agent': 'PostmanRuntime/7.28.4'
    }
    login_json = {
        'email': email,
        'password': str(password),
    }

    res = requests.post(
        login_url, headers=header, json=login_json)
    # print(res.)
    assert res.status_code == 200


def test_create_user_ok():
    print(url)
    r = requests.get(url)

    assert r.status_code == 200


def test_create_user_failed():
    pass


def test_get_user_info_ok():
    pass


def test_get_user_info_failed():
    pass


if __name__ == "__main__":
    pytest.main([__file__])
