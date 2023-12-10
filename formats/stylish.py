def to_str(elem):
    if isinstance(elem, bool):
        if elem:
            return "true"
        else:
            return "false"
    elif elem is None:
        return "null"
    return str(elem)


def make_string(elem, depth, new_string=''):
    space = depth * '    '
    space2 = f"\n{(depth + 1) * '    '}"
    if isinstance(elem, dict):
        for key, vector in elem.items():
            if isinstance(vector, dict):
                new_string += f"{space2}{str(key)}: {make_string(vector, depth + 1)}"
            else:
                new_string += f"{space2}{str(key)}: {to_str(vector)}"
        return f"{{{new_string}\n{space}}}"
    else:
        return to_str(elem)


def stylish(elements, depth=1):
    result = []
    for element in elements:
        name = element['name']
        value = element.get('value')
        new_value = element.get('new_value')
        status = element['status']

        indent = '    ' * (depth - 1)
        space = '    ' * depth

        if status == 'dict':
            result.append(f"{space}{name}: {stylish(value, depth + 1)}")

        elif status == 'added':
            result.append(f"{indent}  + {name}: {make_string(value, depth)}")

        elif status == 'deleted':
            result.append(f"{indent}  - {name}: {make_string(value, depth)}")

        elif status == 'updated':
            result.append(f"{indent}  - {name}: {make_string(value, depth)}")
            result.append(f"{indent}  + {name}: {make_string(new_value, depth)}")


        elif status == 'unchanged':
            result.append(f"{space}{name}: {make_string(value, depth)}")
        else:
            raise ValueError("Unknown status")

    return "{\n" + "\n".join(result) + f"\n{indent}}}"
