
SEPARATOR = " "
ADD = '+ '
DELETE = '- '


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
            lines.append(f"{indent}  {key}: {formatted_value}")
        formatted_string = '\n'.join(lines)
        end_indent = SEPARATOR * (spaces_count + 2)
        return f"{{\n{formatted_string}\n{end_indent}}}"
    else:
        return f"{value}"


def make_stylish_result(diff, spaces_count=2):
    lines = []

    for key, item in diff.items():
        key_name = key
        action = item['type']
        indent = ' ' * spaces_count

        if action == "unchanged":
            current_value = to_str(item.get('value'), spaces_count)
            lines.append(f"{indent}  {key_name}: {current_value}")

        elif action == "modified":
            old_value = to_str(item.get('old_value'), spaces_count)
            new_value = to_str(item.get('new_value'), spaces_count)
            lines.extend([
                f"{indent}- {key_name}: {old_value}",
                f"{indent}+ {key_name}: {new_value}"
            ])

        elif action in ["deleted", "added"]:
            value = to_str(item.get('value'), spaces_count)
            sign = '-' if action == "deleted" else '+'
            lines.append(f"{indent}{sign} {key_name}: {value}")

        elif action == "nested":
            children = make_stylish_result(
                item.get('children', {}),
                spaces_count + 4
            )

            lines.append(f"{indent}  {key_name}: {children}")

    formatted_string = '\n'.join(lines)
    end_indent = ' ' * (spaces_count - 2)

    return f"{{\n{formatted_string}\n{end_indent}}}"
