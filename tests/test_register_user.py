import allure
import pytest
import requests

from data import TestData
from urls import TestEndpoint

class TestRegisterUser:

    @allure.title('Успешная регистрация пользователя')
    def test_register_user_all_valid_data_success(self):
        payload = {
            "email": TestData.email,
            "password": TestData.password,
            "name": TestData.name
        }

        with allure.step('Отправляем запрос на регистрацию'):
            response = requests.post(TestEndpoint.url_register, json=payload)

        assert (response.status_code == TestData.REGISTER_OK["code"] and response.json()["success"] and
                len(response.json()["accessToken"]) > 0 and
                len(response.json()["refreshToken"]) > 0)


    @allure.title('Проверка регистрации существующего пользователя')
    def test_add_duplicate_user_shows_error(self):
        payload = {
            "email": TestData.email,
            "password": TestData.password,
            "name": TestData.name
        }

        with allure.step('Отправляем запрос на регистрацию пользователя'):
            requests.post(TestEndpoint.url_register, json=payload)
        with allure.step('Отправляем повторный запрос на регистрацию того же пользователя'):
            response = requests.post(TestEndpoint.url_register, json=payload)

        assert (response.status_code == TestData.REGISTER_DUPLICATE["code"] and response.json()['success']  == False and
                response.json()['message'] == TestData.REGISTER_DUPLICATE["message"])

    @allure.title('Проверка создания пользователя с невалидными данными')
    @pytest.mark.parametrize('data', [
        TestData.email_and_password, TestData.email_and_name,TestData.password_and_name])
    def test_add_user_not_valid_data(self, data):
        with allure.step('Отправляем запрос на регистрацию пользователя'):
            response = requests.post(TestEndpoint.url_register, json=data)

        assert (response.status_code == TestData.REGISTER_INVALID["code"] and response.json()['success']  == False and
                response.json()['message'] == TestData.REGISTER_INVALID["message"])

