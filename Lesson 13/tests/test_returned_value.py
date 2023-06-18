import pytest
import parse_data as parse_data


@pytest.mark.smoke
class TestReturnedValue:
    def setup_method(self):
        self.parser = parse_data.ParseData()

    def test_returned_value_after_parsing_url(self):
        data = self.parser._get_list_of_urls_from_url('www.google.com')
        assert isinstance(data, list), 'Unexpected datatype returned after parsing URL'

    def test_returned_value_after_parsing_pdf(self):
        data = self.parser._get_list_of_urls_from_pdf('tests/tests_artifacts/1.pdf')
        assert isinstance(data, list), 'Unexpected datatype returned after parsing PDF file'
