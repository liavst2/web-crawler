
from pymongo import MongoClient

class MongoStorage:
  
  def __init__(self):
    self.client = MongoClient("mongodb://localhost:27017/")
    self.db = self.client.pastes