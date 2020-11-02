
from multiprocessing import Queue, Process
from datetime import datetime
from bs4 import BeautifulSoup
import dateparser
import requests
import os
import time


class PasteFetcher(Process):

    def __init__(self, base_url: str, queue: Queue):
        super().__init__()
        self._queue = queue
        self._base_url = base_url
        self._interval = int(os.environ["SAMPLE_INTERVAL"])

    def run(self) -> None:
        # Beginning of time - fetch all recent pastes first
        self._fetch_pastes(fetch_all=True)
        while 1:
            time.sleep(self._interval)
            self._fetch_pastes()

    def _fetch_pastes(self, fetch_all=False):
        self._debug("Fetching another set of pastes...")
        now = datetime.utcnow()

        # getting the HTML template
        response = requests.get(self._base_url)
        response.raise_for_status()

        # parsing HTML template
        soup = BeautifulSoup(response.text, "html.parser")
        pastes = soup.find("ul", {"class": "sidebar__menu"}).findAllNext("li")
        paste_count = 0
        for paste in pastes:
            try:
                paste_date = paste.div.text.split("\n")[3].strip()
                paste_date = dateparser.parse(paste_date, settings={'TIMEZONE': 'UTC'})
                # Skip if it's older than the current interval
                if not fetch_all and (now - paste_date).seconds > self._interval:
                    continue
                paste_key = paste.a.attrs["href"]
                self._queue.put({"url": self._base_url + paste_key, "date": paste_date})
                paste_count += 1
            except Exception as err:
                print(f"Failed to parse paste. Skipping...\n{err}")
        self._debug(f"Uploaded {self._queue.qsize()} pastes")

    def _debug(self, msg):
        print(f"{self.__class__.__name__}::{msg}")

