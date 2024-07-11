import sys


def main(*args: list):
    path, *args = args
    cmd = cmd.strip().lower()

    user_input = input('Enter a command: ')
    command, *args = parse_input(user_input)

    if command in ['close', 'exit']:
        ...
    elif command in ['hello', 'hi']:
        ...
    elif command == 'add':
        ...
    elif command == 'change':
        ...
    elif command == 'phone':
        ...
    elif command == 'all':
        ...
    else:
        ...


def parse_log_line(line: str) -> dict:
    ...


def load_logs(file_path: str) -> list:
    ...


def filter_logs_by_level(logs: list, level: str) -> list:
    ...


def count_logs_by_level(logs: list) -> dict:
    ...


def display_log_counts(counts: dict):
    ...


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)

