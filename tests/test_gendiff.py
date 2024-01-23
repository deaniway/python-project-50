import pytest
from gendiff import generate_diff
import os


def get_fixture_path(file_name):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', file_name)


def get_result_data(expected_result):
    with open(expected_result, "r") as correct:
        return correct.read()


@pytest.mark.parametrize("file1, file2", [
    ('file1.json', 'file2.json'),
    ('file1.yml', 'file2.yml')
])
def test_generate_diff(file1, file2):
    path1 = get_fixture_path(file1)
    path2 = get_fixture_path(file2)

    expected_stylish = get_result_data(get_fixture_path('result_stylish.txt'))
    result_stylish = generate_diff(path1, path2, 'stylish')
    assert result_stylish == expected_stylish

    expected_plain = get_result_data(get_fixture_path('result_plain.txt'))
    result_plain = generate_diff(path1, path2, 'plain')
    assert result_plain == expected_plain

    expected_json = get_result_data(get_fixture_path('result_json.txt'))
    result_json = generate_diff(path1, path2, 'json')
    assert result_json == expected_json
