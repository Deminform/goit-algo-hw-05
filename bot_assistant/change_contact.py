from colorama import Fore, Style, init
from is_person_exist import is_person_exist
from is_valid_phone_number import is_valid_phone_number


def change_contact(args: list, contacts: list):
    init(autoreset=True)

    if len(args) != 2:
        return Fore.YELLOW + 'Incorrect format. Enter in format' + Style.BRIGHT + ' "command Name Phone".'

    name, phone = args
    if not is_valid_phone_number(phone):
        return Fore.YELLOW + 'Incorrect phone number.'

    if is_person_exist(name, contacts):
        for person in contacts:
            if person['name'].lower() == name.lower():
                person['phone'] = phone
                return Fore.GREEN + 'Contact updated.'
    return Fore.YELLOW + 'Username not found.'
