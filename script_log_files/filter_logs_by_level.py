

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda line: line['level'] == level, logs))
