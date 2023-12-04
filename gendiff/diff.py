from gendiff.read_files import read_data

'''
def format_diff(diff):
    lines = []
    for key, value in diff.items():
        lines.append(f'{key}: {value}')
    return '{\n  ' + '\n  '.join(lines) + '\n}'


def generate_diff(file_path1, file_path2):
    data1 = read_data(file_path1)
    data2 = read_data(file_path2)

    diff = {}

    all_keys = set(data1.keys()) | set(data2.keys())

    for key in sorted(all_keys):
        value1 = data1.get(key)
        value2 = data2.get(key)

        if value1 == value2:
            diff[f'  {key}'] = value1
        elif key in data1 and key not in data2:
            diff[f'- {key}'] = value1
        elif key in data2 and key not in data1:
            diff[f'+ {key}'] = value2
        else:
            diff[f'- {key}'] = value1
            diff[f'+ {key}'] = value2

    return format_diff(diff)

'''


from gendiff.read_files import read_data

def format_diff(diff):
    def stringify(value, depth):
        if not isinstance(value, dict):
            return str(value)

        lines = []
        for key, val in value.items():
            if isinstance(val, dict):
                formatted_val = stringify(val, depth + 1)
                lines.append(f"{' ' * (depth * 4)}{key}: {formatted_val}")
            else:
                sign = '+' if str(val).startswith('{') else ('-' if str(val).startswith('-') else ' ')
                lines.append(f"{' ' * (depth * 4 - 2)}{sign} {key}: {str(val).lower()}")

        return "{\n" + "\n".join(lines) + f"\n{' ' * (depth * 4 - 4)}}}"

    return stringify(diff, 1)



def generate_diff(file_path1, file_path2):
    data1 = read_data(file_path1)
    data2 = read_data(file_path2)

    def build_diff(data1, data2):
        diff = {}
        keys = set(data1.keys()) | set(data2.keys())

        for key in sorted(keys):
            if key not in data1:
                diff[f"{key}"] = data2[key] if isinstance(data2[key], dict) else str(data2[key])
            elif key not in data2:
                diff[f"{key}"] = data1[key] if isinstance(data1[key], dict) else str(data1[key])
            elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
                diff[f"{key}"] = build_diff(data1[key], data2[key])
            elif data1[key] == data2[key]:
                diff[f"{key}"] = data1[key] if isinstance(data1[key], dict) else str(data1[key])
            else:
                diff[f"{key}"] = data1[key] if isinstance(data1[key], dict) else str(data1[key])
                diff[f"{key}"] = data2[key] if isinstance(data2[key], dict) else str(data2[key])

        return diff

    diff = build_diff(data1, data2)
    return format_diff(diff)


