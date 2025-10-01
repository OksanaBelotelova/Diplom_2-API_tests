from src.stocks_api import StocksApi
from data import ExistingUser

class TestLoginUser:
    
    def test_successful_user_login(self):
        body = ExistingUser.ExistingUser
        response = StocksApi.user_login(json = body)

        assert response.status_code == 200
        assert response.json()["success"] == True


    def test_login_user_with_wrong_password(self):
        body = ExistingUser.User_with_wrong_password
        response = StocksApi.user_login(json = body)

        assert response.status_code == 401
        assert response.json() == {
                            "message": "email or password are incorrect", 
                            "success": False
                            }


    def test_login_user_with_wrong_email(self):
        body = ExistingUser.User_with_wrong_email
        response = StocksApi.user_login(json = body)

        assert response.status_code == 401
        assert response.json() == {
                            "message": "email or password are incorrect", 
                            "success": False
                            }


    def test_login_user_without_email(self):
        body = ExistingUser.User_without_email
        response = StocksApi.user_login(json = body)

        assert response.status_code == 401
        assert response.json() == {
                            "message": "email or password are incorrect", 
                            "success": False
                            }
    
    
    def test_login_user_without_password(self):
        body = ExistingUser.User_without_password
        response = StocksApi.user_login(json = body)

        assert response.status_code == 401
        assert response.json() == {
                            "message": "email or password are incorrect", 
                            "success": False
                            }