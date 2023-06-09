import unittest
import requests
from vistas import *
from modelos import *
import json
import random

globalList_schema = GlobalListSchema()
user_schema = UserSchema()
n=random.random()
email="adminTest"+str(n)+"@nn.com"
blocked="pruebaTest" + str(n)

class DriverTestCase(unittest.TestCase):
    

    # def test_passing(self):
    #     assert (1, 2, 3) == (1, 2, 3)

    def test_create_blacklist(self):
        requetsLogin = requests.post('http://entrega.us-east-2.elasticbeanstalk.com/api/auth/login', json={
            "username": "admin1",
            "password": "admin1"
        })
        
        requetsPost = requests.post('http://entrega.us-east-2.elasticbeanstalk.com/api/black-list', 
                                     headers={'Authorization': 'Bearer '+ requetsLogin.json()["token"]}, json={
            "email": email,
            "blocked_reason": blocked
        })
        # self.assertIsNotNone(requetsPost.json()["id"])
    
    def test_get_blacklist(self):
        requetsLogin = requests.post('http://entrega.us-east-2.elasticbeanstalk.com/api/auth/login', json={
            "username": "admin1",
            "password": "admin1"
        })
        
        
        requetsGet = requests.get('http://entrega.us-east-2.elasticbeanstalk.com/api/black-list/'+email, 
                                     headers={'Authorization': 'Bearer '+ requetsLogin.json()["token"]})
        
        
        
        self.assertIsNotNone(requetsGet.json())
        self.assertEqual(requetsGet.json(), "El email sí está en la lista negra")
        


if __name__ == "__main__":
    unittest.main()
