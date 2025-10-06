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
    
class ResponseMessage:
    user_already_exist_message = {
                        "success": False,
                        "message": "User already exists"
                        }   
    
    required_field_is_not_filled_message = {
                        "success": False,
                        "message": "Email, password and name are required fields"
                        }
    email_or_password_are_incorrect_message = {
                        "message": "email or password are incorrect", 
                        "success": False
                        }
    email_already_exist_message = {
                        "success": False,
                        "message": "User with such email already exists"
                        }
    user_should_be_authorised_message = {
                        "success": False,
                        "message": "You should be authorised"
                        }
    ingredient_must_be_provided = {
                        "success": False,
                        "message": "Ingredient ids must be provided"
                        }