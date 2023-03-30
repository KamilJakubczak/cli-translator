from abc import ABC


class Translator(ABC):

    @staticmethod
    def translate(word: str) -> str:
        raise NotImplemented
