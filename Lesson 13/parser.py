import argparse
import re
import os
from Data.texts_data import TextData as TEXT
from Data.patterns_data import PatternsData as PATTERN


class Parser:

    @staticmethod
    def __is_matching_data(data):
        if re.match(PATTERN.URL_PATTERN, data):
            return '-url', data
        elif os.path.exists(data):
            return '-pdf', data
        raise Exception(TEXT.INVALID_URL_OR_PDF_TEXT)

    def _parse_data(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-url', type=str, help=TEXT.URL_HELPER)
        parser.add_argument('--pdf', type=str, help=TEXT.PDF_HELPENR)
        data = parser.parse_args()
        if data.url is not None:
            return self.__is_matching_data(data.url)
        elif data.pdf is not None:
            return self.__is_matching_data(data.pdf)
        else:
            new_data = input(TEXT.NO_DATA_ENTERED)
            return self.__is_matching_data(new_data)
