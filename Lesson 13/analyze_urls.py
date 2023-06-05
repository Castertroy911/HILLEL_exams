from parse_html import ParseHTML


class UrlAnalyzer(ParseHTML):

    def _get_broken_urls(self):
        broken_urls = str()
        list_of_urls = self._get_list_of_urls()
        print('Please wait, parsing and saving invalid links 🔄')
        for i in list_of_urls:
            response = self._go_to_url(i)
            if response.status_code != 200:
                broken_urls += f'{i}\n'
        return broken_urls

    def _get_valid_urls(self):
        valid_urls = str()
        list_of_urls = self._get_list_of_urls()
        print('Please wait, parsing and saving valid links 🔄')
        for i in list_of_urls:
            response = self._go_to_url(i)
            if response.status_code == 200:
                valid_urls += f'{i}\n'
        return valid_urls
