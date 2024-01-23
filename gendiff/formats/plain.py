def to_str(value):
    if value is None:
        return 'null'
    elif isinstance(value, (list, dict)):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value


def make_plain_result(diff):
    def _iter(diff, path=''):
        res = []
        for key, data in diff.items():
            current_path = f'{path}.{key}' if path else key
            match data['type']:
                case 'added':
                    value = to_str(data['value'])
                    res.append(
                        f"Property '{current_path}' "
                        f"was added with value: {value}"
                    )
                case 'deleted':
                    res.append(f"Property '{current_path}' was removed")

                case 'modified':
                    new_value = to_str(data['new_value'])
                    old_value = to_str(data['old_value'])
                    res.append(
                        f"Property '{current_path}' was updated. "
                        f"From {old_value} to {new_value}"
                    )
                case 'nested':
                    children = data['children']
                    res.extend(_iter(children, current_path))

                case 'unchanged':
                    pass

                case _:
                    raise ValueError(f"Unsupported node type at {current_path}")

        return res

    return '\n'.join(_iter(diff))
# если  не прописать  unchanged и проигнорировать
# то все впадает  сразу в исключение дефолта
# не догадываюсь как обойти этот момент
