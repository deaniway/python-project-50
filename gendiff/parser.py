import yaml
import json
from gendiff.utilits import get_file_format, get_file_content


def parser_data(content, formats):
    match formats:
        case 'json':
            return json.loads(content)
        case 'yml' | 'yaml':
            return yaml.safe_load(content)
        case default:
            raise ValueError(f"Формат не поддерживается: {formats}")


def parser_data_file(file_path):
    formats = get_file_format(file_path)
    content = get_file_content(file_path)
    return parser_data(content, formats)
