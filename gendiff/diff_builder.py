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
