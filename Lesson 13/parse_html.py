from parser import Parser
import requests
import re


class ParseHTML(Parser):
    LINK_PATTERN = r'(https?:\/\/[\da-z\.-]+\.[a-z\.]{2,6}[\/\w\.-]*)\/?'
    HTTPS_PATTERN = r'(https?:\/\/)'

    def __go_to_url(self, url):
        if re.search(self.HTTPS_PATTERN, url) is None:
            page = requests.get(f'https://{url}')
        else:
            page = requests.get(url)
        return page

    def __get_list_of_urls(self):
        url = self._parse_url()
        url = self.__go_to_url(url)
        list_of_urls = re.findall(self.LINK_PATTERN, url.text)
        return list_of_urls

    @staticmethod
    def __save_valid_urls(url):
        with open(f'valid links.txt', 'w+') as file:
            file.write(f'{url}\n')

    @staticmethod
    def __save_broken_urls(url):
        with open(f'broken links.txt', 'w+') as file:
            file.write(f'{url}')

    """Можно было бы не писать две метода выше, а просто в конструкции if открывать файл и записывать в него данные.
    Но тогда возникнет проблема.Нам нужно будет либо все время открывать файл в режима a+, либо при использовании
    режима w+ он просто будет каждый раз перезаписываться. Поэтому было решено собирать валидные и не валидные линки
    в переменные, а затем записывать даннеы из этих переменных в соответствующие файлы."""
    def save_urls(self):
        valid_urls = str()
        broken_urls = str()
        list_of_urls = self.__get_list_of_urls()
        print('Please wait, URL parsing in progress 🔄')
        for i in list_of_urls:
            response = self.__go_to_url(i)
            if response.status_code == 200:
                valid_urls += f'{i}\n'
            else:
                broken_urls += f'{i}\n'
        ParseHTML.__save_valid_urls(valid_urls)
        ParseHTML.__save_broken_urls(broken_urls)
