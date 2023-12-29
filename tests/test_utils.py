import os
import json


def read_file(file_name):
    fixture_path = os.path.join('tests', 'fixtures', f'{file_name}')
    with open(fixture_path) as file:
        return file.read()


def get_input_data(file_name):
    return json.loads(read_file(file_name))


def get_expected_result(file_name):
    return read_file(file_name)


'''
from gendiff.generate_diff_tree import generate_diff
import pytest
import os


TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


def build_fixture_path(file_name):
    return os.path.join(FIXTURES_PATH, file_name)


def get_content(addres):
    with open(addres, 'r') as f:
        data = f.read()
        return data


@pytest.mark.parametrize("file_path1,file_path2,style,file_name", [
    ('file_json1.json',
     'file_json2.json',
     'stylish',
     'expected.txt'),
    ('file_yaml1.yml',
     'file_yaml2.yml',
     'stylish',
     'expected.txt'),
    ('file_yaml1.yml',
     'file_json2.json',
     'stylish',
     'expected.txt'),
    ('file_json3.json',
     'file_json4.json',
     'stylish',
     'expected_empty_files.txt'),
    ('file_json3.json',
     'file_json1.json',
     'stylish',
     'expected_empty_one_file.txt'),
    ('file_json1.json',
     'file_json3.json',
     'stylish',
     'expected_empty_tow_file.txt'),
    ('file_json5.json',
     'file_json6.json',
     'stylish',
     'expected_tree.txt'),
    ('file_json5.json',
     'file_json6.json',
     'plain',
     'expected_tree_plain.txt'),
    ('file_json1.json',
     'file_json2.json',
     'plain',
     'expected_plain.txt'),
    ('file_json3.json',
     'file_json1.json',
     'plain',
     'expected_empty_one_file_plain.txt'),
    ('file_json1.json',
     'file_json3.json',
     'plain',
     'expected_empty_tow_file_plain.txt'),
    ('file_json5.json',
     'file_json6.json',
     'json',
     'expected_tree_json.txt')])
def test_generate_diff(file_path1, file_path2, style, file_name):
    answer = get_content(build_fixture_path(file_name))
    path1 = build_fixture_path(file_path1)
    path2 = build_fixture_path(file_path2)
    assert generate_diff(path1, path2, style) == answer


@pytest.mark.parametrize("file_path1,file_path2,style,exception, exc_message", [
    ('file_json1.json',
     'file_json2.json',
     'stylis',
     ValueError,
     "Unknown extension"),
    ('file_json.txt',
     'file_yaml.txt',
     'stylish',
     ValueError,
     "Invalid format entered")])
def test_generate_diff_exeption(file_path1, file_path2, style, exception, exc_message):
    path1 = build_fixture_path(file_path1)
    path2 = build_fixture_path(file_path2)
    with pytest.raises(exception) as exception:
        generate_diff(path1, path2, style)
        assert exc_message == exception.value
'''