import pytest
from src.stocks_api import StocksApi
from data import Order

class TestCreateOrder:

    def test_create_successful_order_authorized_user(self,login_user):
        user = login_user
        body = Order.order
        response = StocksApi.create_order(headers={'Authorization': f'{user['accessToken']}'},json=body)
        
        assert response.status_code == 200
        assert response.json()["success"] == True
        
        
        
    def test_create_order_authorized_user_without_ingredients(self,login_user):
        user = login_user
        body = Order.empty_order
        response = StocksApi.create_order(headers={'Authorization': f'{user['accessToken']}'},json=body)
        
        assert response.status_code == 400
        assert response.json()== {
                                "success": False,
                                "message": "Ingredient ids must be provided"
                                }

    def test_create_order_authorized_user_wrong_ingredients(self,login_user):
        user = login_user
        body = Order.wrong_order
        response = StocksApi.create_order(headers={'Authorization': f'{user['accessToken']}'},json=body)
        
        assert response.status_code == 500
        


    @pytest.mark.xfail(reason='response.status_code == 401 this a bug')    
    def test_create_successful_order_unauthorized_user(self,login_user): 
        user = login_user
        body = Order.order
        response = StocksApi.create_order(json=body)
        
        #баг - неавторизованный пользователь может сделать заказ
        assert response.status_code == 401
        assert response.json() == {
                                "success": false,
                                "message": "You should be authorised"
                                }
        