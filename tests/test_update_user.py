from src.stocks_api import StocksApi
from helpers import Generate
from data import ResponseMessage
import allure

class TestUpdateUser:
    
    @allure.title('Изменение имени авторизованного пользователя')
    @allure.description('Авторизованный пользователь может изменить имя')
    def test_update_authorized_user_update_name(self,login_user):
        user = login_user
        body = Generate.update_user_name(self,user['user']['email'])
        response = StocksApi.update_user(headers={'Authorization': f'{user['accessToken']}'},json=body)
        
        assert response.status_code == 200
        assert response.json()["success"] == True
        assert response.json()['user']['email'] == body['email']
        

    @allure.title('Изменение имейла авторизованного пользователя')
    @allure.description('Авторизованный пользователь может изменить имейл')
    def test_update_authorized_user_update_email(self,login_user):
        user = login_user
        body = Generate.update_user_email(self,user['user']['name'])
        response = StocksApi.update_user(headers={'Authorization': f'{user['accessToken']}'},json=body)
        
        assert response.status_code == 200
        assert response.json()["success"] == True
        assert response.json()['user']['name'] == body['name'] 

    @allure.title('Изменение имейла авторизованного пользователя')
    @allure.description('Авторизованный пользователь не может изменить имейл на уже существующий')
    def test_update_authorized_user_update_email_on_existing_email(self,login_user):
        user = login_user
        body = Generate.update_user_email_existing(self,user['user']['name'])
        response = StocksApi.update_user(headers={'Authorization': f'{user['accessToken']}'},json=body)
        
        assert response.status_code == 403
        assert response.json() == ResponseMessage.email_already_exist_message
    
    
    @allure.title('Изменение имени неавторизованного пользователя')
    @allure.description('Неавторизованный пользователь не может изменить имя')
    def test_update_unauthorized_user_update_name(self, login_user):
        user = login_user
        body = Generate.update_user_name(self,user['user']['email'])
        response = StocksApi.update_user(json=body)

        assert response.status_code == 401
        assert response.json() == ResponseMessage.user_should_be_authorised_message

    
    @allure.title('Изменение имейла неавторизованного пользователя')
    @allure.description('Неавторизованный пользователь не может изменить имейл')
    def test_update_unauthorized_user_update_email(self, login_user):
        user = login_user
        body = Generate.update_user_email(self,user['user']['name'])
        response = StocksApi.update_user(json=body)

        assert response.status_code == 401
        assert response.json() == ResponseMessage.user_should_be_authorised_message