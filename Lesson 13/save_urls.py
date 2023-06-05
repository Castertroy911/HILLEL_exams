from analyze_urls import UrlAnalyzer


class SaveUrls(UrlAnalyzer):

    def save_valid_urls(self):
        urls_list = self._get_valid_urls()
        with open(f'valid links.txt', 'w+') as file:
            file.write(f'{urls_list}\n')

    def save_broken_urls(self):
        urls_list = self._get_broken_urls()
        with open(f'broken links.txt', 'w+') as file:
            file.write(f'{urls_list}')