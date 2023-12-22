from collections import namedtuple

DiffElement = namedtuple('DiffElement', ['action', 'name', 'new_value', 'old_value', 'children'])


def for_add(key, value):
    return DiffElement(action='added', name=key, new_value=value, old_value=None, children=None)


def for_delete(key, value):
    return DiffElement(action='deleted', name=key, new_value=None, old_value=value, children=None)


def for_unchanged(key, value):
    return DiffElement(action='unchanged', name=key, new_value=value, old_value=value, children=None)


def for_modified(key, value1, value2):
    return DiffElement(action='modified', name=key, new_value=value2, old_value=value1, children=None)


def for_nested(key, value1, value2):
    return DiffElement(action='nested', name=key, new_value=None, old_value=None, children=generate(value1, value2))


def generate(data1, data2):
    keys = set(data1) | set(data2)
    added = set(data2) - set(data1)
    deleted = set(data1) - set(data2)

    diff = []

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in added:
            diff.append(for_add(key, value2))
        elif key in deleted:
            diff.append(for_delete(key, value1))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(for_nested(key, value1, value2))
        elif value1 != value2:
            diff.append(for_modified(key, value1, value2))
        else:
            diff.append(for_unchanged(key, value1))

    sorted_diff = sorted(diff, key=lambda x: x.name)

    return sorted_diff
