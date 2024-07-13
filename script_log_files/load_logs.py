from parse_log_line import parse_log_line
from decorator import input_error


@input_error
def load_logs(file_path: str) -> list:
    with open(file_path, 'r') as read_file:
        return [parse_log_line(line) for line in read_file]
