from decorator import input_error


@input_error
def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_list = list(filter(lambda line: line['level'] == level, logs))
    if filtered_list:
        return filtered_list
    else:
        raise ValueError(f'Level "{level}" is missing from the log file')
