SEPARATOR = " "
ADD = '+ '
DELETE = '- '
NONE = '  '


def to_str(value, spaces_count=2):
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        indent = SEPARATOR * (spaces_count + 4)
        lines = []
        for key, inner_value in value.items():
            formatted_value = to_str(inner_value, spaces_count + 4)
            lines.append(f"{indent}{NONE}{key}: {formatted_value}")
        formatted_string = '\n'.join(lines)
        end_indent = SEPARATOR * (spaces_count + 2)
        return f"{{\n{formatted_string}\n{end_indent}}}"
    else:
        return f"{value}"


# обработка с пустым словарем был костыль)
def make_stylish_result(diff, spaces_count=2):

    indent = SEPARATOR * spaces_count
    lines = []

    for item in diff:
        key_name = item['key']
        action = item['type']

        match action:
            case "unchanged":
                current_value = to_str(item['value'], spaces_count)
                lines.append(f"{indent}{NONE}{key_name}: {current_value}")

            case "modified":
                old_value = to_str(item['old_value'], spaces_count)
                new_value = to_str(item['new_value'], spaces_count)
                lines.extend([
                    f"{indent}{DELETE}{key_name}: {old_value}",
                    f"{indent}{ADD}{key_name}: {new_value}"
                ])

            case "deleted":
                old_value = to_str(item['value'], spaces_count)
                lines.append(f"{indent}{DELETE}{key_name}: {old_value}")

            case "added":
                new_value = to_str(item['value'], spaces_count)
                lines.append(f"{indent}{ADD}{key_name}: {new_value}")

            case "nested":
                children = make_stylish_result(item['children'], spaces_count + 4)
                lines.append(f"{indent}{NONE}{key_name}: {children}")

    formatted_string = '\n'.join(lines)
    end_indent = SEPARATOR * (spaces_count - 2)

    return f"{{\n{formatted_string}\n{end_indent}}}"


def format_diff_stylish(data):
    return make_stylish_result(data)
