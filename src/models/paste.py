
from datetime import datetime


class Paste(object):

    _UNKNOWN_AUTHOR_FORM = ["Guest", "Unknown", "Anonymous", ""]
    _UNKNOWN_TITLE_FORM = ["Unknown", "No title", "Untitled", ""]

    _UNKNOWN_AUTHOR_DEFAULT = "Unnamed author"
    _UNKNOWN_TITLE_DEFAULT = "Untitled"

    def __init__(self,
                 author: str,
                 title: str,
                 content: str,
                 date: datetime):
        self.author = author
        self.title = title
        self.content = content
        self.date = date

    def normalize(self):
        return dict(
            author=self.author if self.author not in self._UNKNOWN_AUTHOR_FORM else self._UNKNOWN_AUTHOR_DEFAULT,
            title=self.title if self.title not in self._UNKNOWN_TITLE_FORM else self._UNKNOWN_TITLE_DEFAULT,
            content=self.content,
            date=self.date.strftime("%Y-%m-%d %H:%M:%S")
        )
