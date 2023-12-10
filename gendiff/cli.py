import argparse
from gendiff.diff import generate_diff
from formats.stylish import stylish
from gendiff.read_files import open_file, parsing_files


string = 'Compares two configuration files and shows a difference.'
parser = argparse.ArgumentParser(description=string)
parser.add_argument('first_file', help='what about first file')
parser.add_argument('second_file', help='what about second file')
parser.add_argument(
    "-f", "--format", default="stylish",
    help="output format, default: 'stylish'"
)
args = parser.parse_args()


def main_arg():
    file1_data, file1_format = open_file('tests/fixtures/file1.json')
    parsed_file1_data = parsing_files(file1_data, file1_format)
    file2_data, file2_format = open_file('tests/fixtures/file2.json')

    parsed_file2_data = parsing_files(file2_data, file2_format)
    diff = generate_diff(parsed_file1_data, parsed_file2_data)

    formatted_result = stylish(diff)
    print(formatted_result)


if __name__ == '__main__':
    main_arg()
