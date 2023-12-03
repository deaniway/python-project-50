import json
import yaml


def read_data(file_path):
    file_path = str(file_path)
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.safe_load(file)
        else:
            raise ValueError("Неподдерживаемый формат файла. Поддерживаются только JSON и YAML.")
