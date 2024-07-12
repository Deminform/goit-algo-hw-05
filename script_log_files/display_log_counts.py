from prettytable import PrettyTable
from colorama import Fore, Style


def display_log_counts(counts: dict):
    table = PrettyTable()
    table.align = 'l'
    table.field_names = ['Рівень логування', 'Кількість']

    for key, value in counts.items():
        table.add_row([coloring(key), value])
    return table


def coloring(text: str):
    match text:
        case 'INFO':
            return Fore.GREEN + text + Style.RESET_ALL
        case 'DEBUG':
            return Fore.BLUE + text + Style.RESET_ALL
        case 'ERROR':
            return Fore.RED + text + Style.RESET_ALL
        case 'WARNING':
            return Fore.YELLOW + text + Style.RESET_ALL
        case _:
            return text


