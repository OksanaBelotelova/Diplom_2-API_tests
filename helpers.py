import random
import string
from data import ExistingUser

class Generate:

    def generate_random_string(self):
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        return random_string

    def generate_random_user(self):
        user = Generate()
        username = user.generate_random_string()
        email = f'{username}@mail.com'
        password = user.generate_random_string()
        payload = {
            "email": email,
            "password": password,
            "name": username
            }
        return payload
    
    def generate_user_without_email(self):
        user = Generate()
        username = user.generate_random_string()
        password = user.generate_random_string()
        payload = {
            "email": '',
            "password": password,
            "name": username
            }
        return payload
    
    def generate_user_without_name(self):
        user = Generate()
        username = user.generate_random_string()
        email = f'{username}@mail.com'
        password = user.generate_random_string()
        payload = {
            "email": email,
            "password": password,
            "name": ''
            }
        return payload
    
    def generate_user_without_password(self):
        user = Generate()
        username = user.generate_random_string()
        email = f'{username}@mail.com'
        payload = {
            "email": email,
            "password": '',
            "name": username
            }
        return payload
    
    def update_user_name(self,email):
        user = Generate()
        new_name = user.generate_random_string()
        payload = {
            "email": email,
            "name": new_name
            }
        return payload
    
    def update_user_email(self, name):
        user = Generate()
        username = user.generate_random_string()
        new_email = f'{username}@mail.com'
        payload = {
            "email": new_email,
            "name": name
            }
        return payload
    
    def update_user_email_existing(self,name):
        payload = {
            "email": ExistingUser.ExistingUser['email'],
            "name": name
            }
        return payload