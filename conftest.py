import pytest
from src.stocks_api import StocksApi
from helpers import Generate
from data import ExistingUser

@pytest.fixture
def login_user():
    user = Generate()
    body = user.generate_random_user()
    StocksApi.create_user(json = body)
    response = StocksApi.user_login(json = body)
    return response.json
    # yield login_user() 
    # StocksApi.delete_user(headers={'Authorization': f'{response['accessToken']}'})

@pytest.fixture
def login_existing_user():
    body = ExistingUser.ExistingUser
    return StocksApi.user_login(json = body).json()
