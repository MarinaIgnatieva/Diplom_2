from faker import Faker

from helper import generate_random_string
from tests.conftest import new_user


class TestData:
    fake = Faker()
    email = generate_random_string(10) + '@ya.ru'
    password = fake.password(10)
    name = fake.name()


    email_and_password = [email, password]
    email_and_name = [email, name]
    password_and_name = [password, name]

    LOGIN_OK = {
        "code": 200
    }
    LOGIN_INVALID = {
        "code": 401,
        "message": "email or password are incorrect"
    }

    ORDER_OK = {
        "code": 200
    }
    ORDER_WITHOUT_AUTH = {
        "code": 302,
        "location": "/login"
    }
    ORDER_INVALID_INGR = {
        "code": 500
    }
    ORDER_WITHOUT_INGR = {
        "code": 400,
        "message": "Ingredient ids must be provided"
    }

    REGISTER_OK = {
        "code": 200
    }
    REGISTER_DUPLICATE = {
        "code": 403,
        "message": "User already exists"
    }
    REGISTER_INVALID = {
        "code": 403,
        "message": "Email, password and name are required fields"
    }





