import pytest
import random
import string
import requests
from urls.urls import Urls

@pytest.fixture()
def user_register_random_data():
    random_email = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    random_password = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    random_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    random_data = {"email": random_email + "@mail.com", "password": random_password, "name": random_name}
    requests.post(Urls.URL_USER_REGISTER, data=random_data)
    return random_data

@pytest.fixture()
def user_token():
    random_email = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    random_password = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    random_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    random_data = {"email": random_email + "@mail.com", "password": random_password, "name": random_name}
    repost = requests.post(Urls.URL_USER_REGISTER, data=random_data)
    return {**random_data, "accessToken": repost.json()["accessToken"], "refreshToken": repost.json()["refreshToken"],}