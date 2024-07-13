import uuid
from colorama import Fore, Style, init
from is_valid_phone_number import is_valid_phone_number
from is_person_exist import is_person_exist
from decorators import input_error


@input_error
def add_contact(args: list, contacts: list):
    init(autoreset=True)

    name, phone = args

    if is_person_exist(name, contacts):
        raise ValueError(Fore.YELLOW + 'The username is already taken.')

    if not is_valid_phone_number(phone):
        raise ValueError(Fore.YELLOW + 'Incorrect phone number.')

    contacts.append({
        'id': str(uuid.uuid4()),
        'name': name,
        'phone': phone})
    return Fore.GREEN + 'Contact added.'
