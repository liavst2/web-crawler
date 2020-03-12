

from engine.crawler import Crawler
import os
import sys

def main(url):
  try:
    crawler = Crawler(url)
    crawler.start()
    crawler.join()
  except KeyboardInterrupt:
    print("Crawler is stopping gracefully...")
    sys.exit(0)

if __name__ == "__main__":
  url = os.environ["BASE_URL"]
  main(url)
