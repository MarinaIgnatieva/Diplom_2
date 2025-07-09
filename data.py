from faker import Faker

from helper import generate_random_string


class TestEndpoint():

    url_burger = "https://stellarburgers.nomoreparties.site/api"
    url_register = f"{url_burger}/auth/register"
    url_login = f"{url_burger}/auth/login"
    url_order = f"{url_burger}/orders"
    url_logout = f"{url_burger}/auth/logout"
    url_ingredients = f"{url_burger}/ingredients"

class TestData():
    fake = Faker()
    email = generate_random_string(10) + '@ya.ru'
    password = fake.password(10)
    name = fake.name()


    email_and_password = [email, password]
    email_and_name = [email, name]
    password_and_name = [password, name]







