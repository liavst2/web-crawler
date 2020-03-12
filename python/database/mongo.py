
from pymongo import MongoClient

class MongoStorage:
  
  def __init__(self):
    self.client = MongoClient("mongodb://localhost:27017/")
    self.db = self.client.crawler

  def insert_one(self, doc):
    self.db.pastes.insert_one(doc)

  def insert_many(self, docs):
    self.db.pastes.insert_many(docs)
