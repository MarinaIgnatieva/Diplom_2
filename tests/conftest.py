import pytest
import requests

from faker import Faker
from data import TestEndpoint
from helper import generate_random_string


@pytest.fixture
def new_user():

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    fake = Faker()
    email = generate_random_string(10)+'@ya.ru'
    password = fake.password(10)
    name = fake.name()

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(TestEndpoint.url_register, json=payload)


    # если регистрация прошла успешно (код ответа 200), добавляем в список логин и пароль курьера
    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
    else:
        print(response.content)

    # возвращаем список
    return login_pass

@pytest.fixture()
def login(new_user):
    tokens = []
    login_pass = new_user

    payload = {
        "email": login_pass[0],
        "password": login_pass[1]
    }

    response = requests.post(TestEndpoint.url_login, json=payload)

    if response.status_code == 200:
        tokens.append(response.json()["accessToken"])
        tokens.append(response.json()["refreshToken"])
    else:
        print(response.content)

    return tokens

@pytest.fixture()
def list_ingr():
    list = []

    response = requests.get(TestEndpoint.url_ingredients)
    if response.status_code == 200:
        for ingr in response.json()["data"]:
            list.append(ingr["_id"])

    return list