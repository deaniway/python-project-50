from gendiff.engie import DiffElement, generate
from gendiff.formats.stylish import make_stylish_result


def test_make_stylish_result():
    diff = generate({'key1': 'value1'}, {'key2': 'value2'})

    expected_result = '{\n  - key1: value1\n  + key2: value2\n}'

    result = make_stylish_result(diff)

    assert result == expected_result


def test_make_stylish_result_empty_input():
    diff = []

    expected_result = '{}'

    result = make_stylish_result(diff)

    assert result == expected_result


def test_make_stylish_result_nested_items():
    diff = [
        DiffElement(action='nested', name='parent', new_value=None, old_value=None, children=[
            DiffElement(action='added', name='child1', new_value='value1', old_value=None, children=None),
            DiffElement(action='modified', name='child2', new_value='new_value', old_value='old_value', children=None)
        ])
    ]

    expected_result = '{\n  parent: {\n    + child1: value1\n    - child2: old_value\n    + child2: new_value\n  }\n}'

    result = make_stylish_result(diff)

    assert result == expected_result