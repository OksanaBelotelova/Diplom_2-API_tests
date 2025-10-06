from src.stocks_api import StocksApi
from helpers import Generate
from data import ResponseMessage
import allure

class TestCreateUser:
    
    @allure.title('Создание нового юзера')
    @allure.description('При отправке корректного запроса на создание нового юзера приходит ответ об успешном создании с кодом 200')
    def test_create_new_user(self):
        body = Generate.generate_random_user(self)
        response = StocksApi.create_user(json = body)
        
        assert response.status_code == 200
        assert response.json()["success"] == True
        assert response.json()['user']['email'] == body['email']
        assert response.json()['user']['name'] == body['name']


    @allure.title('Cоздание пользователя, который уже зарегистрирован')
    @allure.description('При попытке создать пользователя, который уже зарегистрирован, приходит ответ с кодом 403')
    def test_create_already_existing_user(self):
        body = Generate.generate_random_user(self)
        StocksApi.create_user(json = body)
        response = StocksApi.create_user(json = body)
        
        assert response.status_code == 403
        assert response.json() == ResponseMessage.user_already_exist_message
        

    @allure.title('Создание пользователя, с незаполненным email')
    @allure.description('При попытке создать при пользователя с незаполненным email, приходит ответ с кодом 403')
    def test_create_user_without_email(self):
        body = Generate.generate_user_without_email(self)
        
        response = StocksApi.create_user(json = body)

        assert response.status_code == 403
        assert response.json() == ResponseMessage.required_field_is_not_filled_message
        
    
    @allure.title('Создание пользователя, с незаполненным именем')
    @allure.description('При попытке создать при пользователя с незаполненным именем, приходит ответ с кодом 403')
    def test_create_user_without_name(self):
        body = Generate.generate_user_without_name(self)
        response = StocksApi.create_user(json = body)

        assert response.status_code == 403
        assert response.json() == ResponseMessage.required_field_is_not_filled_message


    @allure.title('Создание пользователя, с незаполненным паролем')
    @allure.description('При попытке создать при пользователя с незаполненным паролем, приходит ответ с кодом 403')  
    def test_create_user_without_password(self):
        body = Generate.generate_user_without_password(self)
        response = StocksApi.create_user(json = body)

        assert response.status_code == 403
        assert response.json() == ResponseMessage.required_field_is_not_filled_message