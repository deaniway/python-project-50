def to_str(value):  # неправльное добавление изменение, вкидывает везде null
    if isinstance(value, (list, dict)):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def make_plain_result_item(item, path=''):
    current_key = item['key']
    current_path = f"{path}.{current_key}" if path else current_key
    action = item['type']
    new_value = to_str(item.get('new_value'))
    old_value = to_str(item.get('old_value'))

    match action:
        case 'added':
            return f"Property '{current_path}' was added with value: {new_value}"
        case 'deleted':
            return f"Property '{current_path}' was removed"
        case 'modified':
            return (
                f"Property '{current_path}' was updated. "
                f"From {old_value} to {new_value}"
            )
        case 'nested':
            children = item.get('children')
            if children is not None:
                return make_plain_result(children, current_path)
            else:
                raise ValueError("Не поддерживается формат ноды")


def make_plain_result(diff, path=''):
    result = []
    for item in diff:
        formatted_item = make_plain_result_item(item, path)
        if formatted_item is not None:
            result.append(formatted_item)

    return '\n'.join(result)


def format_diff_plain(data):
    return make_plain_result(data)
