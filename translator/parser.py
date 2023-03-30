from abc import ABC, abstractmethod
from bs4 import BeautifulSoup as bs


class HtmlParser(ABC):

    def __init__(self, html) -> None:
        self.raw_html = html
        self.soup = self.parse_html()

    def parse_html(self) -> bs:
        soup = bs(self.raw_html, 'html.parser')
        return soup

    @abstractmethod
    def get_translation(self):
        raise NotImplemented
