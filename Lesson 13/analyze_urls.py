from parse_data import ParseData
from Data.texts_data import TextData as TEXT


class UrlAnalyzer(ParseData):

    def _get_urls(self, data):
        if data[0] == '-url':
            list_of_urls = self._get_list_of_urls_from_url(data[1])
        elif data[0] == '-pdf':
            list_of_urls = self._get_list_of_urls_from_pdf(data[1])
        return list_of_urls

    def _analyze_urls(self, data):
        urls = {'valid': [], 'broken': []}
        list_of_urls = self._get_urls(data)
        print(TEXT.PARSING_LINKS)
        for i in list_of_urls:
            response = self._go_to_url(i)
            if response is None or response.status_code != 200:
                urls.get('broken').append(f'{i}\n')
            elif response is not None and response.status_code == 200:
                urls.get('valid').append(f'{i}\n')
        return urls


    '''Здесь причина та же, что и в файле save_urls.py. Хотел сократить количество повторяющегося кода и ускорить 
    работу программы. После того, как ты проверишь ДЗ - сделаю коммит и удалю старые куски кода.'''

    # def _get_urls(self, data):
    #     broken_urls = str()
    #     if data[0] == '-url':
    #         list_of_urls = self._get_list_of_urls_from_url(data[1])
    #     elif data[0] == '-pdf':
    #         list_of_urls = self._get_list_of_urls_from_pdf(data[1])
    #     print(TEXT.PARSING_BROKEN_LINKS)
    #     for i in list_of_urls:
    #         response = self._go_to_url(i)
    #         if response is None or response.status_code != 200:
    #             broken_urls += f'{i}\n'
    #     return broken_urls

    # def _get_urls(self, data):
    #     valid_urls = str()
    #     if data[0] == '-url':
    #         list_of_urls = self._get_list_of_urls_from_url(data[1])
    #     elif data[0] == '-pdf':
    #         list_of_urls = self._get_list_of_urls_from_pdf(data[1])
    #     print(TEXT.PARSING_VALID_LINKS)
    #     for i in list_of_urls:
    #         response = self._go_to_url(i)
    #         if response is not None and response.status_code == 200:
    #             valid_urls += f'{i}\n'
    #     return valid_urls
