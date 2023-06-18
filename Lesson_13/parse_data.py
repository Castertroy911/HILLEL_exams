from parser import Parser
import requests
import re
from pdfminer.high_level import extract_text
from Data.patterns_data import PatternsData as PATTERN


class ParseData(Parser):

    def _go_to_url(self, url):
        if re.search(PATTERN.HTTPS_PATTERN, url) is None:
            page = requests.get(f'https://{url}')
        else:
            try:
                page = requests.get(url)
            except requests.exceptions.ConnectionError:
                return None
        return page

    def _get_list_of_urls_from_url(self, data):
        data_url = self._go_to_url(data)
        list_of_urls = re.findall(PATTERN.LINK_PATTERN, data_url.text)
        return list_of_urls

    @staticmethod
    def _get_list_of_urls_from_pdf(data):
        text = extract_text(data)
        list_of_urls = re.findall(PATTERN.LINK_PATTERN, text)
        return list_of_urls

