
from multiprocessing import Process

class Crawler(Process):
  def __init__(self, url):
    self.crawl_url = url
    self.timeout = 10 # sample the site every 10 seconds

