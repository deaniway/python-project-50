def generate_diff(data1, data2, key=None):
    diff = []
    keys = set(data1.keys()) | set(data2.keys())
    for value in sorted(keys):

        if value not in data1:
            diff.append(
                {"name": value,
                 "value": data2[value],
                 "status": "added"}
            )

        elif value not in data2:
            diff.append(
                {"name": value,
                 "value": data1[value],
                 "status": "deleted"}
            )

        elif isinstance(data1[value], dict) and isinstance(data2[value], dict):
            diff.append(
                {"name": value,
                 "value": generate_diff(data1[value], data2[value], key=value),
                 "status": "dict"}
            )

        elif data1[value] == data2[value]:
            diff.append(
                {"name": value,
                 "value": data1[value],
                 "status": "unchanged"}
            )

        else:
            diff.append(
                {"name": value,
                 "old_value": data1[value],
                 "new_value": data2[value],
                 "status": "updated"}
            )
    return diff
