import pytest
from src.stocks_api import StocksApi
from helpers import Generate

@pytest.fixture
def login_user():
    user = Generate()
    body = user.generate_random_user()
    StocksApi.create_user(json = body)
    return StocksApi.user_login(json = body).json()
    
    