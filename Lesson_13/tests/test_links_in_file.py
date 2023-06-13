import pytest
import requests
from data import PathData


@pytest.mark.smoke
class TestLinksInFile:
    def test_links_in_valid_file(self):
        with open(PathData.PATH_TO_VALID_FILE, "r+") as file:
            for i in file.readlines():
                i = i.rstrip()
                assert requests.get(i).status_code == 200, 'Broken link in file with valid links'

    def test_links_in_broken_file(self):
        with open(PathData.PATH_TO_BROKEN_FILE, "r+") as file:
            a = file.readlines()
            if len(a) > 0:
                for i in a:
                    i = i.rstrip()
                    try:
                        response = requests.get(i)
                        assert response.status_code != 200, 'Valid links in file with broken links'
                    except requests.exceptions.ConnectionError:
                        pass
            else:
                pass
