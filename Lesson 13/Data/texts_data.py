from dataclasses import dataclass


@dataclass
class TextData:
    INVALID_URL_OR_PDF_TEXT: str = f'Entered URL is not valid or Path does not exists. Please run file again and ' \
                                   f'enter valid URL or Absolute path to PDF file! \nValid URL should starts with ' \
                                   f'"www.". or example "www.google.com"'
    URL_HELPER: str = f'URL of the website that need to be parsed'
    PDF_HELPENR: str = f'Path to PDF file that need to be parsed'
    NO_DATA_ENTERED: str = f"Please, specify the URL or Absolute path to PDF file that need to be parsed. " \
                           f"This value shouldn't be blank!!!\n"
    PARSING_LINKS: str = f'Please wait, parsing and saving links 🔄'
