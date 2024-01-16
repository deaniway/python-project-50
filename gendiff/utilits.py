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
