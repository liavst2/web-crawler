
import sys
import requests
from multiprocessing import Process
from threading import Timer
from bs4 import BeautifulSoup
from models.paste import Paste
from database.mongo import MongoStorage

class Crawler(Process):

  def __init__(self, url):
    super().__init__()
    self.crawl_url = requests.get(url).content
    self.timeout = 2 # sample the site every 10 seconds
    self.storage = MongoStorage()
    self.init()

  def init(self):
    Timer(self.timeout, self.crawel).start()


  def crawel(self):
    soup = BeautifulSoup(self.crawl_url, "html.parser")
    pastes = soup.find("ul", { "class": "right_menu" }).findAllNext("li")
    for paste in pastes:
      title = paste.find("a").text
      userTag = paste.find("span").text.split("|")
      user = "Unknown" if len(userTag) == 1 else userTag[0]
      self.storage.insert_one(Paste(user, title).__dict__)
    Timer(self.timeout, self.crawel).start()

