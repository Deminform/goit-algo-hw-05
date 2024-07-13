import re
from decorator import input_error


@input_error
def parse_log_line(line: str) -> dict:
    pattern = r'(\d*-\d+-\d+) (\d+:\d+:\d+) (\S+) (.*)'
    match = re.match(pattern, line)

    if not match:
        raise ValueError(f"Incorrect format of file strings: {line}")

    return {
        'date': match.group(1),
        'time': match.group(2),
        'level': match.group(3),
        'message': match.group(4),
    }
