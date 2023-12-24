def generate_diff_element(action, key, new_value=None,
                          old_value=None, children=None):
    return {
        'action': action,
        'name': key,
        'new_value': new_value,
        'old_value': old_value,
        'children': children
    }


def generate(data1, data2):
    keys = set(data1) | set(data2)
    added = set(data2) - set(data1)
    deleted = set(data1) - set(data2)

    diff = []

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in added:
            diff.append(
                generate_diff_element('added', key, new_value=value2)
            )

        elif key in deleted:
            diff.append(
                generate_diff_element('deleted', key, old_value=value1)
            )

        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(
                generate_diff_element(
                    'nested', key, children=generate(value1, value2)
                )
            )

        elif value1 != value2:
            diff.append(
                generate_diff_element(
                    'modified', key, new_value=value2, old_value=value1)
            )

        else:
            (diff.append
                (generate_diff_element(
                    'unchanged', key, new_value=value1, old_value=value1)))

    sorted_diff = sorted(diff, key=lambda x: x['name'])

    return sorted_diff
