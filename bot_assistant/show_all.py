from colorama import Fore, Style, init


def show_all(contacts: list) -> str:
    init(autoreset=True)
    persons_list = ''
    for person in contacts:
        persons_list += (
            f'Name: {person['name']}, '
            f'Phone: {person['phone']}, '
            f'id: {person["id"]}.\n'
        )
    return Fore.YELLOW + 'No records yet' if len(contacts) == 0 else persons_list
