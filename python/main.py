

from engine.crawler import Crawler
import os
import sys

def main(url):
  crawler = Crawler(url)
  crawler.start()
  crawler.join()

if __name__ == "__main__":
  try:
    url = os.environ["URL"]
    main(url)
  except KeyError:
    print("Please set the environment variable URL")
    sys.exit(1)
