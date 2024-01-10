def generate_diff_element(action, key, new_value=None,
                          old_value=None, children=None):
    diff = {'key': key}

    try:
        match action:
            case 'added':
                diff.update({'type': 'added', 'value': new_value})
            case 'deleted':
                diff.update({'type': 'deleted', 'value': old_value})
            case 'modified':
                diff.update({'type': 'modified', 'new_value': new_value, 'old_value': old_value})
            case 'nested':
                diff.update({'type': 'nested', 'children': children})
            case _:
                diff.update({'type': 'unchanged', 'value': old_value})
    except Exception as e:
        print(f'Error when generating element:{e}')

    return diff


def generate(data1, data2):
    diff = []

    try:
        keys = sorted(data1.keys() | data2.keys())

        for key in keys:
            value1 = data1.get(key)
            value2 = data2.get(key)

            try:
                if key not in data1:
                    diff.append(generate_diff_element('added', key, new_value=value2))

                elif key not in data2:
                    diff.append(generate_diff_element('deleted', key, old_value=value1))

                elif isinstance(value1, dict) and isinstance(value2, dict):
                    diff.append(
                        generate_diff_element('nested', key, children=generate(value1, value2))
                    )

                elif value1 != value2:
                    diff.append(
                        generate_diff_element('modified', key, new_value=value2, old_value=value1)
                    )

                else:
                    diff.append(
                        generate_diff_element('unchanged', key, new_value=value1, old_value=value1)
                    )
            except Exception as e:
                print(f"Error generating difference: {e}")
    except Exception as e:
        print(f"Error generating difference: {e}")

    return diff
