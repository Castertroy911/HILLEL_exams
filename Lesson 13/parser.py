import argparse
import re
import logging


class Parser:
    logging.basicConfig(filename='errors log.log', filemode='w', format='%(asctime)s &(levelname)s &(message)s')
    URL_PATTERN = r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6}[\/\w\.-]*)\/?$'

    def __is_matching_url(self, data):
        if re.match(self.URL_PATTERN, data):
            return data
        logging.error('Entered URL is invalid.')
        raise Exception(f'Entered URL is not valid. Please run file again and enter valid URL!'
                        f'\nValid URL should starts with "www.". For example "www.google.com"')

    def _parse_url(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-url', type=str, help='URL of the website that need to be parsed')
        data = parser.parse_args()
        if data.url is None:
            new_data = input(f"Please, specify the URL that need to be parsed. This value shouldn't be blank!!!\n",)
            return self.__is_matching_url(new_data)
        return self.__is_matching_url(data.url)
