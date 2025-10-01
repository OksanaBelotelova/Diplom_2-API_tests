import random
import string
from data import ExistingUser

class Generate:
    
    def generate_random_user(self):
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        email = f'{username}@mail.com'
        password = ''.join(random.choice('0123456789') for i in range(10))
        payload = {
            "email": email,
            "password": password,
            "name": username
            }
        return payload
    
    def generate_user_without_email(self):
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        password = ''.join(random.choice('0123456789') for i in range(10))
        payload = {
            "email": '',
            "password": password,
            "name": username
            }
        return payload
    
    def generate_user_without_name(self):
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        email = f'{username}@mail.com'
        password = ''.join(random.choice('0123456789') for i in range(10))
        payload = {
            "email": email,
            "password": password,
            "name": ''
            }
        return payload
    
    def generate_user_without_password(self):
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        email = f'{username}@mail.com'
        payload = {
            "email": email,
            "password": '',
            "name": username
            }
        return payload
    
    def update_user_name(self,email):
        new_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        payload = {
            "email": email,
            "name": new_name
            }
        return payload
    
    def update_user_email(self, name):
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
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