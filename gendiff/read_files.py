import yaml
import json
from pathlib import Path


def open_file(file_to_find):
    extension = Path(file_to_find).suffix
    if extension == '.json':
        format = 'json'
        data = open(file_to_find)
    elif extension == '.yml' or extension == '.yaml':
        format = 'yaml'
        data = Path(file_to_find).read_text()
    return data, format


def parsing_files(file_to_parse, format):
    if format == 'json':
        return json.load(file_to_parse)
    if format == 'yaml':
        return yaml.safe_load(file_to_parse)
