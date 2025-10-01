from src.stocks_api import StocksApi
from helpers import Generate

class TestCreateUser:
    
    def test_create_new_user(self):
        body = Generate.generate_random_user(self)
        response = StocksApi.create_user(json = body)
        
        assert response.status_code == 200
        assert response.json()["success"] == True
    

    def test_create_already_existing_user(self):
        body = Generate.generate_random_user(self)
        StocksApi.create_user(json = body)
        response = StocksApi.create_user(json = body)
        
        assert response.status_code == 403
        assert response.json() == {
                            "success": False,
                            "message": "User already exists"
                            }   
        

    def test_create_user_without_email(self):
        body = Generate.generate_user_without_email(self)
        response = StocksApi.create_user(json = body)

        assert response.status_code == 403
        assert response.json() == {
                        "success": False,
                        "message": "Email, password and name are required fields"
                        }
        
    
    def test_create_user_without_name(self):
        body = Generate.generate_user_without_name(self)
        response = StocksApi.create_user(json = body)

        assert response.status_code == 403
        assert response.json() == {
                        "success": False,
                        "message": "Email, password and name are required fields"
                        }
        
    def test_create_user_without_password(self):
        body = Generate.generate_user_without_password(self)
        response = StocksApi.create_user(json = body)

        assert response.status_code == 403
        assert response.json() == {
                        "success": False,
                        "message": "Email, password and name are required fields"
                        }