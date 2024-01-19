def to_str(value, spaces_count=2):
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        indent = " " * (spaces_count + 4)
        lines = []
        for key, inner_value in value.items():
            formatted_value = to_str(inner_value, spaces_count + 4)
            lines.append(f"{indent}  {key}: {formatted_value}")
        formatted_string = '\n'.join(lines)
        end_indent = " " * (spaces_count + 2)
        return f"{{\n{formatted_string}\n{end_indent}}}"
    else:
        return f"{value}"


def make_stylish_result(diff, spaces_count=2):
    lines = []

    for key, item in diff.items():
        action = item['type']
        indent = ' ' * spaces_count

        match action:
            case "unchanged":
                current_value = to_str(item['old_value'], spaces_count)
                lines.append(f"{indent}  {key}: {current_value}")

            case "modified":
                old_value = to_str(item.get('old_value'), spaces_count)
                new_value = to_str(item.get('new_value'), spaces_count)
                lines.extend([
                    f"{indent}- {key}: {old_value}",
                    f"{indent}+ {key}: {new_value}"
                ])

            case action if action in ["deleted", "added"]:
                value = to_str(item.get('value'), spaces_count)
                sign = '-' if action == "deleted" else '+'
                lines.append(f"{indent}{sign} {key}: {value}")

            case "nested":
                try:
                    children = make_stylish_result(
                        item.get('children', {}),
                        spaces_count + 4
                    )
                    lines.append(f"{indent}  {key}: {children}")
                except Exception as e:
                    raise ValueError(f"Unsupported node type"
                                     f" 'nested' at {key}: {e}")

    formatted_string = '\n'.join(lines)
    end_indent = ' ' * (spaces_count - 2)

    return f"{{\n{formatted_string}\n{end_indent}}}"
