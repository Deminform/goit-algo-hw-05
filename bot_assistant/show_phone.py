from colorama import Fore, Style, init


def show_phone(args: list, contacts: list):
    init(autoreset=True)

    if not args:
        return Fore.YELLOW + 'Please type a' + Style.BRIGHT + ' Username'

    for person in contacts:
        if person['name'].lower() == args[0].lower():
            return person['phone']
    return Fore.YELLOW + 'Username not found.'
