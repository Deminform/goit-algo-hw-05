import sys
from script_log_files import *


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


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)
