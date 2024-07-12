import sys
from load_logs import load_logs
from count_logs_by_level import count_logs_by_level
from display_log_counts import display_log_counts, coloring
from filter_logs_by_level import filter_logs_by_level


def main(args: list):
    path = args[1]
    list_of_logs = load_logs(path)
    counted_logs = count_logs_by_level(list_of_logs)
    table = display_log_counts(counted_logs)
    print(table)

    if len(args) == 3:
        result = filter_logs_by_level(list_of_logs, args[2].upper())
        print(f"\nДеталі логів для рівня '{coloring(args[2].upper())}':")
        for log in result:
            print(f'{log['date']} {log['time']} - {log["message"]}')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)
