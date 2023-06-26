import os
from lib import load_file


users_file_path = os.path.abspath('./data')
users_file_name = 'users.yaml'

load_users_file = load_file.LoadFile(users_file_path, users_file_name)


def users():
    users_data = load_users_file.read_file()
    return users_data


def login_users():
    current_users = users()
    logged_users = current_users['login_users']
    return logged_users


if __name__ == "__main__":
    print(users())
