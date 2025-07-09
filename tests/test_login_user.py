import requests
import allure

from data import TestEndpoint, TestData
from tests.conftest import new_user


class TestLoginUser():

    @allure.title('Проверка входа под существующим пользователем')
    def test_authorization_existing_user_success(self, new_user):
        login_pass = new_user

        payload = {
            "email": login_pass[0],
            "password": login_pass[1]
        }

        response = requests.post(TestEndpoint.url_login, json = payload)

        assert (response.status_code == 200 and response.json()["success"] and
                len(response.json()["accessToken"]) > 0 and
                len(response.json()["refreshToken"]) > 0)


    @allure.title('Проверка входа с несуществующим email')
    def test_authorization_user_with_nonexisted_email(self, new_user):
        email_nonexisted = TestData.email
        login_pass = new_user

        payload = {
            "email": email_nonexisted,
            "password": login_pass[1]
        }

        response = requests.post(TestEndpoint.url_login, json = payload)

        assert (response.status_code == 401 and response.json()["success"] == False and
                response.json()["message"] == "email or password are incorrect")

    @allure.title('Проверка входа с несуществующим паролем')
    def test_authorization_user_with_nonexisted_password(self, new_user):
        password_nonexisted = TestData.password
        login_pass = new_user

        payload = {
            "email": login_pass[0],
            "password": password_nonexisted
        }

        response = requests.post(TestEndpoint.url_login, json=payload)

        assert (response.status_code == 401 and response.json()["success"] == False and
                response.json()["message"] == "email or password are incorrect")