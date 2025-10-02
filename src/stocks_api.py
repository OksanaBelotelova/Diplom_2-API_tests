import requests
import allure
from data import Endpoint

class StocksApi:
    
    @allure.step("Create user")
    def create_user(*args, **kwargs):
        return requests.post(Endpoint.CREATE_USER, **kwargs)
    
    @allure.step("Login as a user")
    def user_login(*args, **kwargs):
        return requests.post(Endpoint.LOGIN_USER, **kwargs)
    
    @allure.step("Update user")
    def update_user(*args, **kwargs):
        return requests.patch(Endpoint.UPDATE_USER,**kwargs)
    
    @allure.step("Create order")
    def create_order(*args, **kwargs):
        return requests.post(Endpoint.CREATE_ORDER, **kwargs)
    
    @allure.step("Get Order")
    def get_orders(*args,**kwargs):
        return requests.get(Endpoint.GET_ORDER,**kwargs)
    
    @allure.step("Delete User")
    def delete_user(*args,**kwargs):
        return requests.delete(Endpoint.DELETE_USER,**kwargs)
        