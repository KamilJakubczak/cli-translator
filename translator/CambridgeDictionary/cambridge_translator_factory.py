
from .cambridge_parser import DefinitionParse, TranslationParse
from .cambridge_urls import CambridgeDefUrlGenerator, CambridgeEngGerUrlGenerator, CambridgeEngPolUrlGenerator
from .cambridge_translator import CambridgeTranslator
from translator.factory import TranslatorFactory
from translator.translator import Translator


class CambridgeTranslatorFactory(TranslatorFactory):
    
    def create_translator(self, way: str, text: str) -> Translator:
        if way == 'DEF':
            url_generator = CambridgeDefUrlGenerator
            parser = DefinitionParse
            return CambridgeTranslator(url_generator, parser)

        if way == 'ENG-POL':
            url_generator = CambridgeEngPolUrlGenerator
            parser = TranslationParse
            return CambridgeTranslator(url_generator, parser)

        if way == 'ENG-GER':
            url_generator = CambridgeEngGerUrlGenerator
            parser = TranslationParse
            return CambridgeTranslator(url_generator, parser)
        

