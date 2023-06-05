from analyze_urls import UrlAnalyzer


class SaveUrls(UrlAnalyzer):

    '''Решил здесь объеденить два метода в один и сделать его более универсальным. Плюс сократил количество методов и кода.
    Это помогло добиться большей скорости работы, так как раньше программа пробегалась по всему спыску ссылок 2 раза,
    соответственно по 2 раза происходил get запрос на каждую ссылку. Из-за этого работа была медленной. Сейчас ссылок
    немного, но если таких ссылок будет тысячи или десятки тысяч, то скорость работы будет в 2 раза быстрее. Оставил
    закомментированные куски кода. Я знаю, что это плохая практика, но это просто чтобы ты увидел, что я это реализовывал.
    Как проверишь ДЗ, я сделаю новый коммит и удалю старые куски кода.'''

    # def __save_valid_urls(self, data):
    #     urls_list = self._get_valid_urls(data)
    #     with open(f'valid links.txt', 'w+') as file:
    #         file.write(f'{urls_list}\n')
    #
    # def __save_broken_urls(self, data):
    #     urls_list = self._get_broken_urls(data)
    #     with open(f'broken links.txt', 'w+') as file:
    #         file.write(f'{urls_list}')

    def save_urls(self):
        data = self._parse_data()
        urls_list = self._analyze_urls(data)
        with open(f'valid links.txt', 'w+') as file:
            file.writelines(urls_list.get('valid'))
        with open(f'broken links.txt', 'w+') as file:
            file.writelines(urls_list.get("broken"))
