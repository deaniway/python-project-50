SEPARATOR = " "
ADD = '+ '
DELETE = '- '
NONE = '  '


def to_str(value, spaces_count=2):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()

    if isinstance(value, dict):
        indent = SEPARATOR * (spaces_count + 4)
        lines = []

        for key, inner_value in value.items():
            lines.append(
                f"{indent}{NONE}{key}: {to_str(inner_value, spaces_count + 4)}"
            )

        formatted_string = '\n'.join(lines)
        end_indent = SEPARATOR * (spaces_count + 2)
        return f"{{\n{formatted_string}\n{end_indent}}}"
    return f"{value}"


def format_element(item, spaces_count):
    key_name = item['name']
    action = item['action']

    if action == "unchanged":
        current_value = to_str(item['new_value'], spaces_count)
        return f"{SEPARATOR * spaces_count}{NONE}{key_name}: {current_value}"

    elif action == "modified":
        old_value = to_str(item['old_value'], spaces_count)
        new_value = to_str(item['new_value'], spaces_count)
        return (f"{SEPARATOR * spaces_count}{DELETE}{key_name}:"
                f" {old_value}\n"
                f"{SEPARATOR * spaces_count}{ADD}{key_name}: {new_value}")

    elif action == "deleted":
        old_value = to_str(item['old_value'], spaces_count)
        return f"{SEPARATOR * spaces_count}{DELETE}{key_name}: {old_value}"

    elif action == "added":
        new_value = to_str(item['new_value'], spaces_count)
        return f"{SEPARATOR * spaces_count}{ADD}{key_name}: {new_value}"

    elif action == 'nested':
        children = make_stylish_result(item['children'], spaces_count + 4)
        return f"{SEPARATOR * spaces_count}{NONE}{key_name}: {children}"


def make_stylish_result(diff, spaces_count=2):
    if not diff:
        return '{}'
    formatted_elements = [format_element(item, spaces_count) for item in diff]
    formatted_string = '\n'.join(formatted_elements)
    end_indent = SEPARATOR * (spaces_count - 2)
    return f"{{\n{formatted_string}\n{end_indent}}}"


def format_diff_stylish(data):
    return make_stylish_result(data)
