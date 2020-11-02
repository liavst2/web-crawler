
from engines import PasteFetcher, PasteAnalyzer
from multiprocessing import Queue
import sys
import signal


class Crawler:

    def __init__(self):
        self.crawl_url = "https://pastebin.com"
        raw_pastes_queue = Queue()
        self.paste_fetcher = PasteFetcher(self.crawl_url, raw_pastes_queue)
        self.paste_analyzer = PasteAnalyzer(raw_pastes_queue)
        signal.signal(signal.SIGTERM, self.terminate)
        signal.signal(signal.SIGINT, self.terminate)

    def start(self):

        self.paste_fetcher.start()
        self.paste_analyzer.start()

        self.paste_fetcher.join()
        self.paste_analyzer.join()

    def terminate(self, signum, frame):
        self.paste_fetcher.terminate()
        self.paste_analyzer.terminate()
        sys.exit(0)


if __name__ == "__main__":
    crawler = Crawler()
    crawler.start()

