import uuid
from colorama import Fore, Style, init
from is_valid_phone_number import is_valid_phone_number
from is_person_exist import is_person_exist


def add_contact(args: list, contacts: list):
    init(autoreset=True)

    if len(args) != 2:
        return Fore.YELLOW + 'Incorrect format. Enter in format' + Style.BRIGHT + ' "command Name Phone".'

    name, phone = args
    if not is_valid_phone_number(phone):
        return Fore.YELLOW + 'Incorrect phone number.'

    if not is_person_exist(name, contacts):
        contacts.append({
            'id': str(uuid.uuid4()),
            'name': name,
            'phone': phone})
        return Fore.GREEN + 'Contact added.'
    else:
        return Fore.YELLOW + 'Username already taken.'
