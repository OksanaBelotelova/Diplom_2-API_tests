from src.stocks_api import StocksApi
from data import ResponseMessage
import allure

class TestGetOrder:

    @allure.title('Получение заказов конкретного пользователя авторизованным пользователем')
    @allure.description('Авторизованный пользователь может посмотреть свои заказы')
    def test_get_order_authorized_user(self, login_existing_user):
        user = login_existing_user
        response = StocksApi.get_orders(headers={'Authorization': f'{user['accessToken']}'})
        print(response.json())
        assert response.status_code == 200
        assert len(response.json()['orders']) > 0


    @allure.title('Получение заказов конкретного пользователя неавторизованным пользователем')
    @allure.description('Невторизованный пользователь не может посмотреть свои заказы')
    def test_get_order_unauthorized_user(self, login_existing_user):
        user = login_existing_user
        response = StocksApi.get_orders()
        
        assert response.status_code == 401
        assert response.json() == ResponseMessage.user_should_be_authorised_message