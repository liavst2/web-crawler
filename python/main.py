

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
  try:
    url = os.environ["URL"]
    main(url)
  except KeyError:
    print("Please set the environment variable URL")
    sys.exit(1)
