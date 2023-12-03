from gendiff.read_files import read_data


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



