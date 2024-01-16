def generate_diff_element(action, key, new_value=None,
                          old_value=None, children=None):
    diff = {'key': key}

    try:
        match action:
            case 'added':
                diff.update({
                    'type': 'added',
                    'value': new_value
                })
            case 'deleted':
                diff.update({
                    'type': 'deleted',
                    'value': old_value
                })
            case 'modified':
                diff.update({
                    'type': 'modified',
                    'new_value': new_value,
                    'old_value': old_value
                })
            case 'nested':
                diff.update({
                    'type': 'nested',
                    'children': children
                })
            case _:
                diff.update({
                    'type': 'unchanged',
                    'value': old_value
                })
    except Exception as e:
        print(f'Error when generating element:{e}')

    return diff


def generate(data1, data2):
    diff = {}

    keys = sorted(data1.keys() | data2.keys())

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key not in data1:
            diff[key] = {
                'type': 'added',
                'value': data2[key]
            }

        elif key not in data2:
            diff[key] = {
                'type': 'deleted',
                'value': data1[key]
            }

        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = {
                'type': 'nested',
                'children': generate(data1[key], data2[key])
            }

        elif data1[key] != data2[key]:
            diff[key] = {
                'type': 'modified',
                'old_value': data1[key],
                'new_value': data2[key]
            }

        else:
            diff[key] = {
                'type': 'unchanged',
                'old_value': data1[key],
                'new_value': data2[key]
            }

    return diff
