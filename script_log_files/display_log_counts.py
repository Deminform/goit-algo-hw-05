from prettytable import PrettyTable


def display_log_counts(counts: dict):
    table = PrettyTable()
    table.field_names = ['Рівень логування', 'Кількість']

    for key, value in counts.items():
        table.add_row([key, value])
    return table
