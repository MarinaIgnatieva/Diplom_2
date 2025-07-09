from http.client import responses

import requests
import allure

from data import TestEndpoint


class TestOrders():

    @allure.title('Успешное создание заказа авторизованным пользователем существующими ингредиентами')
    def test_add_order_authorized_user_with_existing_ingredients_success(self, login, list_ingr):

        payload = {
            "ingredients":[list_ingr[0], list_ingr[1], list_ingr[2]]
        }

        response = requests.post(TestEndpoint.url_order, json = payload, headers={
            "Authorization": login[0]
        })

        assert (response.status_code == 200 and response.json()["success"] and
                len(response.json()["name"]) > 0
                and response.json()["order"]["number"] > 0)

    @allure.title('Неуспешное создание заказа без авторизации пользователя с существующими ингредиентами')
    def test_add_order_without_authorized_user_with_existing_ingredients_redirect_to_login(self, login, list_ingr):
        payload = {
            "ingredients": [list_ingr[0], list_ingr[1], list_ingr[2]]
        }

        response = requests.post(TestEndpoint.url_order, json=payload)

        assert response.status_code == 302 and response.headers["Location"] == "/login"

    @allure.title('Неуспешное создание заказа авторизованным пользователем с не существующими ингредиентами')
    def test_add_order_authorized_user_nonexicted_ingredients_shows_error(self, login):
        payload = {
            "ingredients": ["70dg467fbb","40nah384hfg2" , "34mdmj21nfn3345"]
        }

        response = requests.post(TestEndpoint.url_order, json=payload, headers={
            "Authorization": login[0]
        })

        assert response.status_code == 500

    @allure.title('Неуспешное создание заказа авторизованным пользователем при отсутствии ингредиентов')
    def test_add_order_authorized_user_and_without_ingredients_shows_error(self, login):
        payload = {
            "ingredients": []
        }

        response = requests.post(TestEndpoint.url_order, json=payload, headers={
            "Authorization": login[0]
        })

        assert (response.status_code == 400 and response.json()["success"] == False and
                response.json()["message"] == "Ingredient ids must be provided")
