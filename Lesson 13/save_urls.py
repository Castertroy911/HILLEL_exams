from analyze_urls import UrlAnalyzer
from parser import Parser


class SaveUrls:
    def save_urls(self, parser: Parser, url_analyzer: UrlAnalyzer):
        data = parser._parse_data()
        urls_list = url_analyzer._analyze_urls(data)
        with open(f'valid links.txt', 'w+') as file:
            file.writelines(urls_list.get('valid'))
        with open(f'broken links.txt', 'w+') as file:
            file.writelines(urls_list.get("broken"))
