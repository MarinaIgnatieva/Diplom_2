import pytest
import requests

from faker import Faker
from urls import TestEndpoint
from helper import generate_random_string


# метод регистрирует нового пользователя и возвращает список из email и пароля
@pytest.fixture
def new_user():

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем email, пароль и имя пользователя
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

    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    response = requests.post(TestEndpoint.url_register, json=payload)


    # если регистрация прошла успешно (код ответа 200), добавляем в список email и пароль пользователя
    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
    

    # возвращаем список
    return login_pass

# метод логинит зарегистрированного пользователя и возвращает список токенов
@pytest.fixture()
def login(new_user):
    # создаём список, чтобы метод мог его вернуть
    tokens = []
    
    #создаем нового пользователя
    login_pass = new_user

    # собираем тело запроса
    payload = {
        "email": login_pass[0],
        "password": login_pass[1]
    }

    # отправляем запрос на авторизацию пользователя и сохраняем ответ в переменную response
    response = requests.post(TestEndpoint.url_login, json=payload)

    # если авторизация прошла успешно (код ответа 200), добавляем в список accessToken и refreshToken
    if response.status_code == 200:
        tokens.append(response.json()["accessToken"])
        tokens.append(response.json()["refreshToken"])

    # возвращаем список
    return tokens

# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
@pytest.fixture()
def list_ingr():
    list = []

    response = requests.get(TestEndpoint.url_ingredients)
    if response.status_code == 200:
        for ingr in response.json()["data"]:
            list.append(ingr["_id"])

    return list