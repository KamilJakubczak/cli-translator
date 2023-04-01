from .translator import Translator


class ContextTranslator:

    def __init__(self, translator_engine: Translator) -> None:
        self._translator_engine = translator_engine

    @property
    def translator_engine(self) -> Translator:
        return self._translator_engine

    @translator_engine.setter
    def translator_engine(self, translator_engine: Translator):
        self._translator_engine = translator_engine

    def translate(self, text: str) -> str:
        return self._translator_engine.translate(text)




