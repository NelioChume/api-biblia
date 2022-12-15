import requests
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost/abibliadigital")
mycol = myclient["customers"]

users =   {
  "name": "NelioChume",
  "email": "chunelio2@gmail.com",
  "password": "654321",
  "notifications": True
}



req = requests.post('https://www.abibliadigital.com.br/api/users')

print(req.text)