# Link analyzer and parser

This project can parse links and generate files with valid and invalid links.

- You can get valid and broken links from URL by launching main.py file with flag -url "_url for parsing_". 
- Also you can extract URLs from PDF file. To do it just launch main.py file with flag --pdf "_name of the pdf file_".

Attention: you need to copy your file to the "Lesson 13/tests/test_artifacts" folder to make possible analyzing PDF file by it's name.

After successful launching you will get 2 files:

- _valid links.txt_
- _broken links.txt_

Required dependencies:

All dependencies are in "[requirements.txt](https://github.com/Castertroy911/HILLEL_exams/commit/62c7304a0eebc72bc69608eddc52bef5c5436d95)" file.
You can install it with the command:
- pip install -r requirements.txt
