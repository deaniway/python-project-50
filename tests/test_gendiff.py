import pytest
from gendiff import generate_diff
import os


def get_fixtures_path(file_name):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', file_name)


def get_data(expected_result):
    with open(get_fixtures_path(expected_result), "r") as correct:
        return correct.read()


@pytest.mark.parametrize("file1, file2", [
    ('file1.json', 'file2.json'),
    ('file1.yml', 'file2.yml')
])
def test_generate_diff(file1, file2):
    path1 = get_fixtures_path(file1)
    path2 = get_fixtures_path(file2)

    assert generate_diff(path1, path2, 'stylish') == get_data('result_stylish')
    assert generate_diff(path1, path2, 'plain') == get_data('result_plain')
    assert generate_diff(path1, path2, 'json') == get_data('result_json')
    assert generate_diff(path1, path2) == get_data('result_stylish')
