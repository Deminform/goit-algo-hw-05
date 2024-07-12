import sys
from script_log_files.load_logs import load_logs
from script_log_files.count_logs_by_level import count_logs_by_level
from script_log_files.filter_logs_by_level import filter_logs_by_level
from script_log_files.display_log_counts import display_log_counts


def main(args: list):
    path = args[2]
    list_of_logs = load_logs(path)
    counted_logs = count_logs_by_level(list_of_logs)
    table = display_log_counts(counted_logs)
    print(table)

    if level := args[3]:
        result = filter_logs_by_level(list_of_logs, level)
        print(f'Деталі логів для рівня "{level}":')
        for log in result:
            print(f'{log['date'], log['time']} - {log["message"]}')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)
