from abc import ABC
from .translator import Translator


class TranslatorFactory(ABC):

    def create_translator(self, *args, **kwargs) -> Translator:
        raise NotImplemented

