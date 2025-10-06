from src.stocks_api import StocksApi
from data import ExistingUser, ResponseMessage
import allure


class TestLoginUser:
    
    @allure.title('Логин под существующим пользователем')
    @allure.description('Существующий юзер удачно осуществляет вход')
    def test_successful_user_login(self):
        body = ExistingUser.ExistingUser
        response = StocksApi.user_login(json = body)

        assert response.status_code == 200
        assert response.json()["success"] == True


    @allure.title('Логин существующего пользователя с неверным паролем')
    @allure.description('Существующий юзер не может осуществляет вход с неверным паролем')
    def test_login_user_with_wrong_password(self):
        body = ExistingUser.User_with_wrong_password
        response = StocksApi.user_login(json = body)

        assert response.status_code == 401
        assert response.json() == ResponseMessage.email_or_password_are_incorrect_message


    @allure.title('Логин существующего пользователя с неверным email')
    @allure.description('Существующий юзер не может осуществляет вход с неверным email')
    def test_login_user_with_wrong_email(self):
        body = ExistingUser.User_with_wrong_email
        response = StocksApi.user_login(json = body)

        assert response.status_code == 401
        assert response.json() == ResponseMessage.email_or_password_are_incorrect_message


    @allure.title('Логин существующего пользователя без emal')
    @allure.description('Существующий юзер не может осуществляет вход без email')
    def test_login_user_without_email(self):
        body = ExistingUser.User_without_email
        response = StocksApi.user_login(json = body)

        assert response.status_code == 401
        assert response.json() ==  ResponseMessage.email_or_password_are_incorrect_message
    

    @allure.title('Логин существующего пользователя без пароля')
    @allure.description('Существующий юзер не может осуществляет вход без пароля')
    def test_login_user_without_password(self):
        body = ExistingUser.User_without_password
        response = StocksApi.user_login(json = body)

        assert response.status_code == 401
        assert response.json() == ResponseMessage.email_or_password_are_incorrect_message