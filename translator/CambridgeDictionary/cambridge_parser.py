from parser import HtmlParser
from errors import AppError


class TranslationParse(HtmlParser):

    def get_translation(self):
        all_occurance = self.soup.find_all('span', class_='trans')
        first_occurence = all_occurance[0]
        return first_occurence.string.strip()


class DefinitionParse(HtmlParser):

    def get_translation(self):
        all_occurance = self.soup.find_all('div', class_='def')
        try:
            first_occurence = all_occurance[0]
        except IndexError:
            raise AppError('Word not found')
        text = ' '.join([f.string.strip() for f in first_occurence.contents])
        return text
