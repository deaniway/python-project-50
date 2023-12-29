
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
            children = item['children']
            return make_plain_result(children, current_path)
        case default:
            raise ValueError(f"Не поддерживаемый формат ноды.")
# давай временно оставим все исключения на русском
# исправлений много меня ждет, проще глазами отследить косяк
# ближе к середине финиша исправим lang)


def make_plain_result(diff, path=''):
    result = filter(None, map(lambda item: make_plain_result_item(item, path), diff))
    return '\n'.join(result)


def format_diff_plain(data):
    return make_plain_result(data)
