class Endpoint:
    CREATE_USER = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    LOGIN_USER = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    UPDATE_USER = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    CREATE_ORDER = 'https://stellarburgers.nomoreparties.site/api/orders'
    GET_ORDER = 'https://stellarburgers.nomoreparties.site/api/orders'
    DELETE_USER = 'https://stellarburgers.nomoreparties.site/api/auth/user'

class ExistingUser:
    ExistingUser  = {
            "email": "Oksanatest@mail.com",
            "password": "password123",
            "name": "Oksanatest"
            }
    User_with_wrong_password = {
            "email": "Oksanatest@mail.com",
            "password": "passw123",
            "name": "Oksanatest"
            }
    
    User_with_wrong_email = {
            "email": "Oksanates@mail.com",
            "password": "password123",
            "name": "Oksanatest"
            }
    
    User_without_email = {
            "email": "",
            "password": "password123",
            "name": "Oksanatest"
            }
    
    User_without_password = {
            "email": "Oksanatest@mail.com",
            "password": "",
            "name": "Oksanatest"
            }
    
class Order:
    order = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa72"]
            }
    empty_order = { "ingredients":''}
    wrong_order = {
            "ingredients": ["61c97ya71d1f82001b", "61c0c5a72001bdaaa70", "61c0cga71d1f82001gdaaa72"]
            }
    
# class ResponseMessage:
    