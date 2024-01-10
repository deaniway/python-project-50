import yaml
import json


def parser_data(content, format_file):
    match format_file:
        case 'json':
            return json.loads(content)
        case 'yml' | 'yaml':
            return yaml.safe_load(content)
        case _:
            raise ValueError(f"Формат не поддерживается: {format_file}")



