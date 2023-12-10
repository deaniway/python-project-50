from pathlib import Path
from gendiff.diff import generate_diff
import yaml

def test_generate_diff(tmp_path):
    # Пути к файлам для сравнения
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    res = 'expected_diff.txt'

    with open(res, 'r') as expected_diff_file:
        expected_diff = expected_diff_file.read()

    generated_result = generate_diff(file_path1, file_path2)
    assert generated_result == res




'''
def test_generate_diff_yaml():
    # Определение путей к файлам
    file1_path = 'tests/fixtures/file1.yaml'
    file2_path = 'tests/fixtures/file2.yaml'
    expected_diff_path = 'tests/fixtures/expected_diff.txt'

    # Чтение ожидаемого результата из файла
    with open(expected_diff_path, 'r') as expected_diff_file:
        expected_diff = expected_diff_file.read()

    # Генерация diff
    generated_diff = generate_diff(file1_path, file2_path)

    assert generated_diff == expected_diff
'''


