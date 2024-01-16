from gendiff.diff_builder import generate
from gendiff.formats import format_diff
from gendiff.parser import parser_data
import os


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


def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = parser_data_file(file_path1)
    data2 = parser_data_file(file_path2)
    diff = generate(data1, data2)
    return format_diff(diff, formatter)
