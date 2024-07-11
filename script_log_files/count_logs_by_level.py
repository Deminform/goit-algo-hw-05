from collections import Counter


def count_logs_by_level(logs: list) -> dict:
    return Counter([result['level'] for result in logs])
