from gendiff.parser import parser_data_file
from gendiff.diff_builder import generate
from gendiff.formats import format_diff


def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = parser_data_file(file_path1)
    data2 = parser_data_file(file_path2)
    diff = generate(data1, data2)
    return format_diff(diff, formatter)
