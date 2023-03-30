from abc import ABC
from CambridgeDictionary.cambridge_translator_factory import CambridgeTranslatorFactory
from factory import TranslatorFactory

class EngineFoctory(ABC):

    def get_engine_factory(self) -> TranslatorFactory:
        raise NotImplemented

class ConcreteEngineFactory(EngineFoctory):

    def get_engine_factory(self, engine: str) -> TranslatorFactory:
        if engine == 'cambridge':
            return CambridgeTranslatorFactory()
        raise ValueError('Wrong translation engine')
