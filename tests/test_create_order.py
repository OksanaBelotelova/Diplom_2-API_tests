import pytest
from src.stocks_api import StocksApi
from data import Order, ResponseMessage
import allure

class TestCreateOrder:
    @allure.title('Создание заказа авторизованным пользователем')
    @allure.description('Авторизованный пользователь может создать заказ')
    def test_create_successful_order_authorized_user(self,login_user):
        user = login_user
        body = Order.order
        response = StocksApi.create_order(headers={'Authorization': f'{user['accessToken']}'},json=body)
        
        assert response.status_code == 200
        assert response.json()["success"] == True
        
        
    @allure.title('Создание пустого заказа авторизованным пользователем')
    @allure.description('Пользователь не может создать пустой заказ') 
    def test_create_order_authorized_user_without_ingredients(self,login_user):
        user = login_user
        body = Order.empty_order
        response = StocksApi.create_order(headers={'Authorization': f'{user['accessToken']}'},json=body)
        
        assert response.status_code == 400
        assert response.json()== ResponseMessage.ingredient_must_be_provided


    @allure.title('Создание заказа авторизованным пользователем с неверным хешем ингредиентов')
    @allure.description('При попытке создать заказ с неверным хешем ингредиентов возращается 500 ошибка') 
    def test_create_order_authorized_user_wrong_ingredients(self,login_user):
        user = login_user
        body = Order.wrong_order
        response = StocksApi.create_order(headers={'Authorization': f'{user['accessToken']}'},json=body)
        
        assert response.status_code == 500
        

    @allure.title('Создание заказа неавторизованным пользователем')
    @allure.description('Неавторизованный пользователь не может создать заказ')
    @pytest.mark.xfail(reason='response.status_code == 401 this a bug')    
    def test_create_successful_order_unauthorized_user(self,login_user): 
        user = login_user
        body = Order.order
        response = StocksApi.create_order(json=body)
        
        #баг - неавторизованный пользователь может сделать заказ
        assert response.status_code == 401
        assert response.json() == ResponseMessage.user_should_be_authorised_message