"""
import pytest
from gendiff.generate_diff import generate_diff
import os


def get_fixture_path(file_name):
    return os.path.join(os.path.dirname(__file__), 'fixtures', file_name)


json1 = get_fixture_path('file1.json')
json2 = get_fixture_path('file2.json')
res_stylish = get_fixture_path('result_stylish.txt')
res_plain = get_fixture_path('result_plain.txt')
res_json = get_fixture_path('result_json.txt')
yaml1 = get_fixture_path('file1.yml')
yaml2 = get_fixture_path('file2.yml')


@pytest.mark.parametrize(("path1", "path2", "style", "expected"),
                         [(json1, json2, 'stylish', res_stylish),
                          (yaml1, yaml2, 'stylish', res_stylish),
                          (json1, json2, 'plain', res_plain),
                          (yaml1, yaml2, 'plain', res_plain),
                          (json1, json2, 'json', res_json),
                          (yaml1, yaml2, 'json', res_json)]
                         )
def test_generate_diff(path1, path2, style, expected):
    with open(expected, "r") as correct:
        assert generate_diff(path1, path2, style) == correct.read()
"""

import pytest
from gendiff.generate_diff import generate_diff
import os


def get_fixture_path(file_name):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', file_name)


@pytest.mark.parametrize("file1, file2", [
    ('file1.json', 'file2.json'),
    ('file1.yml', 'file2.yml')
])
def test_generate_diff(file1, file2):
    path1 = get_fixture_path(file1)
    path2 = get_fixture_path(file2)

    expected_stylish = get_fixture_path('result_stylish.txt')
    result_stylish = generate_diff(path1, path2, 'stylish')
    with open(expected_stylish, "r") as correct:
        assert result_stylish == correct.read()

    expected_plain = get_fixture_path('result_plain.txt')
    result_plain = generate_diff(path1, path2, 'plain')
    with open(expected_plain, "r") as correct:
        assert result_plain == correct.read()

    expected_json = get_fixture_path('result_json.txt')
    result_json = generate_diff(path1, path2, 'json')
    with open(expected_json, "r") as correct:
        assert result_json == correct.read()
