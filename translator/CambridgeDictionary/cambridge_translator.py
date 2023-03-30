from fetcher import get_html
from url_generator import UrlGenerator
from parser import HtmlParser
from translator import Translator


class CambridgeTranslator(Translator):

    def __init__(self, url_generator: UrlGenerator, parser: HtmlParser) -> None:
        self.url_generator = url_generator
        self.parser = parser

    def translate(self, word):
        self.url = self.url_generator.generete_url(word)
        self.fetched_html = get_html(self.url)
        self.parsed = self.parser(self.fetched_html)
        return self.parsed.get_translation()


