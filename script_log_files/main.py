import sys


def main(*args: list):
    path = ''
    cmd_list = []

    if len(args) >= 2:
        path, *commands = args
        cmd_list = commands.strip().lower()

    match cmd_list[0]:
        case 'info':
            ...
        case 'error':
            ...
        case 'debug':
            ...
        case 'warning':
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

