import os
import pytest
from .data import PathData


@pytest.mark.smoke
class TestFilesCreated:
    def test_file_with_valid_links_created(self):
        assert os.path.exists(PathData.PATH_TO_VALID_FILE), 'File is not created'

    def test_file_with_broken_links_created(self):
        assert os.path.exists(PathData.PATH_TO_BROKEN_FILE), 'File is not created'
