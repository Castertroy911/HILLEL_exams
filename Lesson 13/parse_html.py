from parser import Parser
import requests
import re


class ParseHTML(Parser):
    LINK_PATTERN = r'(https?:\/\/[\da-z\.-]+\.[a-z\.]{2,6}[\/\w\.-]*)\/?'
    HTTPS_PATTERN = r'(https?:\/\/)'

    def _go_to_url(self, url):
        if re.search(self.HTTPS_PATTERN, url) is None:
            page = requests.get(f'https://{url}')
        else:
            page = requests.get(url)
        return page

    def _get_list_of_urls(self):
        url = self._parse_url()
        url = self._go_to_url(url)
        list_of_urls = re.findall(self.LINK_PATTERN, url.text)
        return list_of_urls
