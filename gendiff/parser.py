import yaml
import json
import os


def file_format(file_path):
    ignore_name, txt = os.path.splitext(file_path)
    return txt[1:]


def file_content(file_path):
    with open(file_path) as f:
        return f.read()


def parser_data(content, form):
    if form == 'json':
        return json.loads(content)
    if form in ['yml', 'yaml']:
        return yaml.safe_load(content)
    raise ValueError(f"Формат не поддерживается: {form}")


def parser_data_file(file_path):
    form = file_format(file_path)
    content = file_content(file_path)
    return parser_data(content, form)
