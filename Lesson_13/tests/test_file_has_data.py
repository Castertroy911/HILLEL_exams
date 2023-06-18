import logging
import pytest
from .data import PathData


@pytest.mark.smoke
@pytest.mark.test
class TestFileHasData:
    def test_valid_file_has_data(self):
        with open(PathData.PATH_TO_VALID_FILE, "r+") as file:
            logging.info('Read file in "test valid file has data"')
            data = file.readlines()
            assert len(data) > 0, 'File contains no data'

    @pytest.mark.xfail
    def test_broken_file_has_data(self):
        with open(PathData.PATH_TO_BROKEN_FILE, "r+") as file:
            logging.info('Read file in "test broken file has data"')
            data = file.readlines()
            assert len(data) > 0, 'File contains no data'
