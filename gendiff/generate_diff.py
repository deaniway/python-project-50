from gendiff.diff_builder import generate
from gendiff.formats import format_diff
from gendiff.parser import parser_data
import os


def get_file_format(file_path):
    _, ignore_name = os.path.splitext(file_path)
    return ignore_name[1:]


def parser_data_file(file_path):
    _, file_name = os.path.splitext(file_path)
    format_file = file_name[1:]

    with open(file_path) as f:
        content = f.read()

    return parser_data(content, format_file)


def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = parser_data_file(file_path1)
    data2 = parser_data_file(file_path2)
    diff = generate(data1, data2)
    return format_diff(diff, formatter)
