
from pymongo import MongoClient
import os


class MongoStorage:

    def __init__(self):
        address = os.environ["DB_ADDRESS"]
        port = int(os.environ["DB_PORT"])
        self.client = MongoClient(address, port)
        self.db = self.client["crawler"]

    def insert_one(self, doc):
        self.db["pastes"].insert_one(doc)

    def insert_many(self, docs):
        self.db["pastes"].insert_many(docs)
