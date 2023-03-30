from url_generator import UrlGenerator


class CambridgeEngPolUrlGenerator(UrlGenerator):

    @staticmethod
    def generete_url(word: str):
        return f'https://www.dictionary.cambridge.org/dictionary/english-polish/{word}'


class CambridgeEngGerUrlGenerator(UrlGenerator):

    @staticmethod
    def generete_url(word: str):
        return f'https://www.dictionary.cambridge.org/dictionary/english-german/{word}'

class CambridgeDefUrlGenerator(UrlGenerator):

    @staticmethod
    def generete_url(word: str):
        return f'https://www.dictionary.cambridge.org/dictionary/english/{word}'
