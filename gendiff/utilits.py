import os
from gendiff.parser import parser_data


def get_file_format(file_path):
    ignore_name, txt = os.path.splitext(file_path)
    return txt[1:]


def get_file_content(file_path):
    with open(file_path) as f:
        return f.read()


def parser_data_file(file_path):
    format_file = get_file_format(file_path)
    content = get_file_content(file_path)
    return parser_data(content, format_file)


''' 
при переносе этих двух функций в модуль generate_diff возникает ошибка 
связанная с цикллическими импортами,поэтоу создал новый модуль дабы избежать этого момента:

ImportError: cannot import name 'get_file_format' from partially initialized module 'gendiff.generate_diff' 
(most likely due to a circular import) (/Users/way/python-project-50/gendiff/generate_diff.py)

решение, думаю, пока что временное
'''
