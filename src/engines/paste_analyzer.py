
from multiprocessing import Process, Queue
from db.mongo import MongoStorage
from models.paste import Paste
from bs4 import BeautifulSoup
import requests
import time
import os


class PasteAnalyzer(Process):

    def __init__(self, queue: Queue):
        super().__init__()
        self._queue = queue
        self._interval = int(os.environ["ANALYZER_INTERVAL"])
        self._batch_size = int(os.environ["ANALYZER_BATCH_SIZE"])
        self._storage = MongoStorage()

    def run(self) -> None:
        while 1:
            time.sleep(self._interval)
            self._analyze_pastes()

    def _read_queue(self, batch_size: int):
        paste_objects = []
        count = batch_size
        while not self._queue.empty() and count:
            paste_objects.append(self._queue.get(block=True))
            count -= 1
        return paste_objects

    def _analyze_pastes(self):
        self._debug("Searching for pastes to parse...")
        paste_objects = self._read_queue(self._batch_size)
        if not paste_objects:
            self._debug("No pastes to parse yet. Back to sleep...")
            return
        normalized_pastes = []
        for paste_object in paste_objects:
            response = requests.get(paste_object["url"])
            response.raise_for_status()
            # Parse the paste
            soup = BeautifulSoup(response.text, "html.parser")
            try:
                paste_title_el = soup.find("div", {"class": "info-top"})
                paste_author_el = soup.find("div", {"class": "username"})
                paste_content_el = soup.find("textarea", {"class": "textarea"})
                title = paste_title_el.h1.text
                author = paste_author_el.a.text
                raw_content = paste_content_el.text
                normalized_pastes.append(Paste(author, title, raw_content, paste_object["date"]).normalize())
            except Exception as err:
                self._debug(f"Failed to analyze paste. Skipping...\n{err}")
        # Insert results into DB
        self._storage.insert_many(normalized_pastes)

    def _debug(self, msg):
        print(f"{self.__class__.__name__}::{msg}")

