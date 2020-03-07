import string
import pymorphy2
import re
from typing import Iterable
from text_analyzer.common import status_time


class TextFilter:
    def __init__(self, source_stop_words: str = 'stop_words.txt'):
        """
        Class for filtering text

        'stop_words.txt' (default) taken from https://github.com/stopwords-iso/stopwords-ru

        :param source_stop_words: File with stop words
        """
        self.stop_words = set()
        self.add_stop_words_from_file(source_stop_words)

    def add_stop_words(self, added_stop_words: Iterable) -> None:
        """
        Adds stop words from collection

        :param added_stop_words: Collection with stop words
        """
        self.stop_words.update(map(lambda x: x.strip().lower(), added_stop_words))

    def add_stop_words_from_file(self, file_name: str) -> None:
        """
        Adds stop words from file

        :param file_name: File with stop words
        """
        with open(file_name, encoding='utf-8') as input_stop_words:
            self.stop_words.update(map(lambda x: x.strip().lower(), input_stop_words.readlines()))

    @status_time
    def parse_text(self, text: str) -> Iterable:
        """
        Parsing text

        :param text: Text to parse
        :return: Iterator with parsed words
        """
        if type(text) != str:
            raise TypeError(f'Must be str, not ({type(text).__name__})')
        text = self.split_hash_tags(text)
        text = self.text_to_lower(text)
        text = text.replace('ё', 'е')
        text = self.remove_punctuation(text)
        words = self.delete_irrelevant(text)
        words = self.remove_stop_words(words, self.stop_words)
        words = self.transform_words_to_normal_form(words)
        words = self.remove_stop_words(words, self.stop_words)
        return words

    @staticmethod
    @status_time
    def split_hash_tags(text: str) -> str:
        """
        Parsing text with hash tags

        :param text: Text with illegible hash tags
        :return: Text with parsing hash tags
        """
        words = re.findall('#[а-яА-Я]+', text)              # Find all hash tags with '#'
        text = re.sub('#[а-яА-Я]+', ' ', text)              # Delete all hash tags from text
        morph = pymorphy2.MorphAnalyzer()
        for word in words:
            # Parse 'OtherWords' to 'Other words'
            for i in re.findall('[А-Я][а-я]+', word[1:]):
                if 'FakeDictionary' not in map(lambda x: x[0].__class__.__name__, morph.parse(i)[0].methods_stack):
                    text += ' ' + i
        return text

    @staticmethod
    @status_time
    def text_to_lower(text):
        """
        Convert all symbols to lower case

        :param text: Source text
        :return: Converted lowercase text
        """
        return text.lower()

    @staticmethod
    @status_time
    def remove_punctuation(text: str) -> str:
        """
        Replace all punctuation symbols to white space

        :param text: Text with punctuation
        :return: Filtered string
        """
        return ''.join(map(lambda x: ' ' if x in string.punctuation else x, text))

    @staticmethod
    @status_time
    def delete_irrelevant(text: str) -> Iterable:
        """
        Remove links, HTML-tags, etc.

        :param text: Text to filter
        :return: Filtered words
        """
        text = re.sub(r'http(s)?://\S*', ' ', text)     # Remove links
        text = re.sub(r'<.*>', ' ', text)               # Remove HTML tags
        text = re.findall(r'[а-я]+', text)              # Find all [а-я] strings
        return text

    @staticmethod
    @status_time
    def remove_stop_words(words: Iterable, stop_words: Iterable) -> Iterable:
        """
        Remove all stop words from

        :param words: Source list of words
        :param stop_words: Unnecessary words
        :return: Filtered list of words
        """
        return filter(lambda x: x not in stop_words, words)

    @staticmethod
    @status_time
    def transform_words_to_normal_form(words: Iterable) -> Iterable:
        """
        Convert words to normal form

        :param words: Source list of words
        :return: List of normal form words
        """
        morph = pymorphy2.MorphAnalyzer()
        return map(lambda x: morph.parse(x)[0].normal_form, words)
