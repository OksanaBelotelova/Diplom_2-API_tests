from src.stocks_api import StocksApi

class TestGetOrder:

    def test_get_order_authorized_user(self, login_existing_user):
        user = login_existing_user
        response = StocksApi.get_orders(headers={'Authorization': f'{user['accessToken']}'})
        
        assert response.status_code == 200
        assert response.json()["success"] == True

    def test_get_order_unauthorized_user(self, login_existing_user):
        user = login_existing_user
        response = StocksApi.get_orders()
        
        assert response.status_code == 401
        assert response.json() == {
                             "success": False,
                             "message": "You should be authorised"
                            }