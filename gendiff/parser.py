import yaml
import json


def parse_data(data, data_format):
    match data_format:
        case 'json':
            return json.loads(data)
        case 'yml' | 'yaml':
            return yaml.safe_load(data)
        case _:
            raise ValueError(f'Формат не поддерживается: {data_format}')
