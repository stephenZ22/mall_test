
from config import settings
import requests
import pytest
import os
import sys


# setting = settings.Settings()
# print(setting.baseUrl())

# @pytest.mar
url = settings.Settings().testUrl()


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
    test_create_user_ok()
