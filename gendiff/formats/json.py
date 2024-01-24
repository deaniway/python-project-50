import json


def make_json_result(diff):
    return json.dumps(diff, indent=2)
