import pymongo
class User:
    def __init__(self, name, email, password):
        self.conexao(name, email, password)
    def conexao(self, name, email, password):
        self.name = pymongo.mongo_client
        self.email = email
        self.passowrd = password


