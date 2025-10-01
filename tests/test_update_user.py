from src.stocks_api import StocksApi
from helpers import Generate
class TestUpdateUser:
    
    def test_update_authorization_user_update_name(self,login_user):
        user = login_user
        body = Generate.update_user_name(self,user['user']['email'])
        response = StocksApi.update_user(headers={'Authorization': f'{user['accessToken']}'},json=body)
        
        assert response.status_code == 200
        assert response.json()["success"] == True


    def test_update_authorization_user_update_email(self,login_user):
        user = login_user
        body = Generate.update_user_email(self,user['user']['name'])
        response = StocksApi.update_user(headers={'Authorization': f'{user['accessToken']}'},json=body)
        assert response.status_code == 200
        assert response.json()["success"] == True


    def test_update_authorization_user_update_email_on_existing_email(self,login_user):
        user = login_user
        body = Generate.update_user_email_existing(self,user['user']['name'])
        response = StocksApi.update_user(headers={'Authorization': f'{user['accessToken']}'},json=body)
        
        assert response.status_code == 403
        assert response.json() == {
                                "success": False,
                                "message": "User with such email already exists"
                                }
    
    
    def test_update_unauthorized_user_update_name(self, login_user):
        user = login_user
        body = Generate.update_user_name(self,user['user']['email'])
        response = StocksApi.update_user(json=body)

        assert response.status_code == 401
        assert response.json() == {
                            "success": False,
                            "message": "You should be authorised"
                            }