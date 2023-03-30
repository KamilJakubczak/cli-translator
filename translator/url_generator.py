from abc import ABC
from typing import Union


class UrlGenerator(ABC):

    @staticmethod
    def generete_url(word: Union[str, None] = None) -> str:
        raise NotImplemented
